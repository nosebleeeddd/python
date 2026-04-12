#!/usr/bin/env python3

import urllib.parse
import urllib.request

# python3 GET request using standard library
url = 'https://google.com'

with urllib.request.urlopen(url) as response:        #GET request
    content = response.read()

print(content)
