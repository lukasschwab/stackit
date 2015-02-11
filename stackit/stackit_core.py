#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
import sys
import stackexchange
from stackexchange import Sort
# A good testing URL: http://stackoverflow.com/questions/16800049/changepassword-test
# The approved answer ID: 16800090

import requests
import subprocess
import click
import bs4
import os


if sys.version_info[:2] < (3, 0):
    input = raw_input

NUM_RESULTS = 5
# API key is public, according to SO documentation
# (link?)
API_KEY = "3GBT2vbKxgh*ati7EBzxGA(("
VERSION_NUM = "0.1.3"

# HTML to markdown parsing
# https://github.com/aaronsw/html2text
import html2text
h = html2text.HTML2Text()

user_api_key = API_KEY

so = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key, impose_throttling=True)
so.be_inclusive()


class Config():
    """ Main configuration object """
    def __init__(self):
        self.search = False
        self.stderr = False
        self.tag = False
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


def select(questions, num):
    print_full_question(questions[num - 1])
    working = True
    while working:
        user_input = click.prompt("Enter b to launch browser, x to return to search, or q to quit")
        if user_input == 'b':
            click.launch(questions[num - 1].json['link'])
        elif user_input == 'q':
            sys.exit()
        elif user_input == 'x':
            click.echo("\n" * 12)
            # Ranging over the 5 questions including the user's choice
            origin = 0
            if not num % NUM_RESULTS:
                origin = num - NUM_RESULTS
            else:
                origin = num - num % NUM_RESULTS
            for j in range(origin, origin + NUM_RESULTS):
                print_question(questions[j], j + 1)
            working = False
        else:
            click.echo(click.style(
                "The input entered was not recognized as a valid choice.",
                fg="red"))


def focus_question(questions):
    working = True
    while working:
        user_input = click.prompt("Enter m for more, a question number to select, or q to quit")
        if user_input == 'm':
            working = False
        elif user_input == 'q':
            sys.exit()
        elif user_input.isnumeric() and int(user_input) <= len(questions):
            select(questions, int(user_input))
        else:
            click.echo(click.style(
                "The input entered was not recognized as a valid choice.",
                fg="red"))


def _search(config):
    # inform user
    click.echo('Searching for: {0}...'.format(config.term))
    click.echo('Tags: {0}'.format(config.tag))

    questions = so.search_advanced(
        q=config.term,
        tagged=config.tag.split(),
        sort=Sort.Votes)

    count = 0
    question_logs = []
    # quicker way for appending to list
    add_to_logs = question_logs.append
    for question in questions:
        if 'accepted_answer_id' in question.json:
            count += 1
            add_to_logs(question)
            print_question(question, count)
            if count % NUM_RESULTS == 0:
                focus_question(question_logs)
    
    if not questions:
            click.echo(
                click.style("Your search \'{0}\' with tags \'{1}\' returned no results.".format(config.term,config.tag),
                fg="red"))
            

def print_question(question, count):
    # questionurl gives the url of the SO question
    # the answer is under id "answer-answerid", and text of answer is in class post-text
    questionurl = question.json['link']
    answerid = question.json['accepted_answer_id']
    # Pulls the html from the StackOverflow site, converts to Beautiful Soup
    response = requests.get(questionurl)
    soup = bs4.BeautifulSoup(response.text)
    # Prints the accepted answer div, concatonated "answer-" and answerid
    # Gets the p string -- do al answers follow this format, or do some have more info?
    answer = soup.find("div", {"id": "answer-" + str(answerid)}).p

    if answer is None:
        # handle case where no text is provide, just code, like: http://stackoverflow.com/a/1128728/1651228
        answer = soup.find("div", {"id": "answer-" + str(answerid)}).find("div", {"class": "post-text"})

    answer = h.handle(answer.prettify())

    click.echo(''.join([
        click.style(''.join([str(count), '\nQuestion: ', question.title]), fg='blue'),
        ''.join(['\nAnswer', answer]),
    ]))


def get_term(config):
    if config.search:
        return config.search
    elif config.stderr:
        # don't show stdout to user
        with open(os.devnull, 'wb') as DEVNULL:
            process = subprocess.Popen(
                config.stderr,
                stdout=DEVNULL,
                stderr=subprocess.PIPE, shell=True)

        output = process.communicate()[1].splitlines()

        # abort if no error
        if not len(output):
            click.echo(click.style(
                "Your executable does not raise an error.",
                fg="red"))
            sys.exit(1)

        return str(output[-1])
    return ""


def print_full_question(question):
    questionurl = question.json['link']
    answerid = question.json['accepted_answer_id']
    response = requests.get(questionurl)
    soup = bs4.BeautifulSoup(response.text)
    # Focuses on the single div with the matching answerid--necessary b/c bs4 is quirky
    for answerdiv in soup.find_all('div', attrs={'id': 'answer-' + str(answerid)}):
        # Return printable text div--the contents of the answer
        # This isn't perfect; things like code indentation aren't pretty at all
        # print(answerdiv.find('div', attrs={'class': 'post-text'}))
        answertext = h.handle(answerdiv.find('div', attrs={'class': 'post-text'}).prettify())
    for cell in soup.find_all('td', attrs={'class': 'postcell'}):
        questiontext = h.handle(cell.find('div', attrs={'class': 'post-text'}).prettify())

    click.echo(''.join([
        click.style(''.join([
            "-------------------------QUESTION------------------------\n",
            question.title, '\n', questiontext,
        ]), fg='blue'),
        ''.join([
            "\n\n-------------------------------ANSWER------------------------------------\n",
            answertext,
        ]),
    ]))


def search_verbose(term):
    questions = so.search_advanced(q=term, sort=Sort.Votes)
    question = questions[0]
    print_full_question(question)


@click.command()
@click.option("-s", "--search", default="", help="Searches StackOverflow for your query")
@click.option("-e", "--stderr", default="", help="Runs an executable command (i.e. python script.py) and automatically inputs error message to StackOverflow")
@click.option("-t", "--tag", default="", help="Searches StackOverflow for your tags")
@click.option("--verbose", is_flag=True, help="displays full text of most relevant question and answer")
@click.option("--version", is_flag=True, help="displays the version")
@pass_config
def main(config, search, stderr, tag, verbose, version):
    """ Parses command-line arguments for StackIt """
    config.search = search
    config.stderr = stderr
    config.tag = tag
    config.verbose = verbose

    config.term = get_term(config)

    if verbose:
        search_verbose(config.term)
    elif search or stderr:
        _search(config)
    elif version:
        click.echo("Version {VERSION_NUM}".format(**globals()))

if __name__ == '__main__':
    main()
