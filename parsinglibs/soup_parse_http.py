#!/usr/bin/env python3

# parsing request into a tree
# to read elements from HTML
# using BeautifulSoup4

from bs4 import BeautifulSoup as bs
import requests


url = 'https://www.google.com'
response = requests.get(url)    # GET request

tree = bs(response.text, 'html.parser')    # Parse into tree as HTML


# find elements, all 'a' anchor tags elements in this case
for link in tree.find_all('a'):
    print("%s -> %s" % (link.get('href'), link.text))



