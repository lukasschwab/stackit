#!/usr/bin/env python
from __future__ import print_function
import sys
import stackexchange
from stackexchange import Sort
# A good testing URL: http://stackoverflow.com/questions/16800049/changepassword-test
# The approved answer ID: 16800090

import requests
import bs4

# HTML to markdown parsing
# https://github.com/aaronsw/html2text
import html2text
h = html2text.HTML2Text()

so = stackexchange.Site(stackexchange.StackOverflow, impose_throttling=True)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        term = raw_input('Please provide a search term:')
    else:
        term = ' '.join(sys.argv[1:])
    print('Searching for %s... \n' % term,)
    #sys.stdout.flush()

    question = so.search_advanced(q = term, sort = Sort.Votes)[0]

    if 'accepted_answer_id' in question.json:
        questionurl = question.json['link']
        answerid = question.json['accepted_answer_id']

        print ('%8d %s' % (question.id, question.title))
        #questionurl gives the url of the SO question
        #the answer is under id "answer-answerid", and text of answer is in class post-text

        # Pulls the html from the StackOverflow site, converts to Beautiful Soup
        response = requests.get(questionurl)
        soup = bs4.BeautifulSoup(response.text)
        # Prints the accepted answer div, concatonated "answer-" and answerid
        # Gets the p string -- do al answers follow this format, or do some have more info?
        print(h.handle(soup.find("div", {"id": "answer-"+str(answerid)}).p.prettify()))