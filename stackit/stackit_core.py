#!/usr/bin/env python
from __future__ import print_function
import sys
import stackexchange
from stackexchange import Sort
# A good testing URL: http://stackoverflow.com/questions/16800049/changepassword-test
# The approved answer ID: 16800090

import requests
import bs4
import re

NUM_RESULTS = 5
API_KEY = "3GBT2vbKxgh*ati7EBzxGA(("

# HTML to markdown parsing
# https://github.com/aaronsw/html2text
import html2text
h = html2text.HTML2Text()

user_api_key = API_KEY

so = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key, impose_throttling=True)
so.be_inclusive()

def searchTerm(term):
    print('Searching for: %s... \n' % term,)
    questions = so.search_advanced(q = term, sort = Sort.Votes)
    j = 0
    count = 0
    while(j < len(questions)):
        question = questions[j]
        if 'accepted_answer_id' in question.json:
            count+=1
            printQuestion(question, count)
            if(count % NUM_RESULTS == 0):
                more = raw_input("Press m for more, or a number to select: ")
                if(more == 'm'):
                    print('\n')
                    continue
        j+=1


def printQuestion(question, count):
    questionurl = question.json['link']
    answerid = question.json['accepted_answer_id']
    #questionurl gives the url of the SO question
    #the answer is under id "answer-answerid", and text of answer is in class post-text

    # Pulls the html from the StackOverflow site, converts to Beautiful Soup
    response = requests.get(questionurl)
    soup = bs4.BeautifulSoup(response.text)
    # Prints the accepted answer div, concatonated "answer-" and answerid
    # Gets the p string -- do al answers follow this format, or do some have more info?
    print(str(count) + "\n" + "Question: " + question.title + "\nAnswer: " + h.handle(soup.find("div", {"id": "answer-"+str(answerid)}).p.prettify()) + "\n")

def getTerm(args):
    term = ""
    if len(args) < 2:
        term = raw_input('Please provide a search term:')
    elif(args[1] == "-stderr"):
        for line in args[2].splitlines():
            term = line
        print("Term is: " + term)
    else:
        term = ' '.join(args[1:])
    return term

def getFullAnswer(soup, answerid):
    # Focuses on the single div with the matching answerid--necessary b/c bs4 is quirky
    for answerdiv in soup.find_all('div', attrs={'id': 'answer-'+str(answerid)}):
        # Return printable text div--the contents of the answer
        # This isn't perfect; things like code indentation aren't pretty at all
        return foo.find('div', attrs={'class': 'post-text'})

def main():
    term = getTerm(sys.argv)
    searchTerm(term)
    sys.stdout.flush()

    
