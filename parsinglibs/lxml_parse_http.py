#!/usr/bin/env python3

# parsing bytes as HTML tree structure
# to find any link anchor tags

# BytesIO treats bytes as file
# lxml is our parser
# requests sends HTTP requests and gets response

from io import BytesIO
from lxml import etree

import requests

url = 'https://www.google.com'

response = requests.get(url)    # GET request
content = response.content      # content is of type 'bytes'

parser = etree.HTMLParser()             # Parser type

 # Parse data wrapped in BytesIO to treat bytes as file stream using HTML rules
content = etree.parse(BytesIO(content), parser=parser)

# Finding elements on page
for link in content.findall('.//a'):         # Find all anchor tag elements
    print('%s -> %s' % (link.get('href'), link.text))
