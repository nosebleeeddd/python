#!/usr/bin/env python3

import urllib2


# python2 GET request using standard library in bytes
url = 'https://google.com'

reponse = urllib2.urlopen('url')        # GET request

print(response.read())
response.close()

###########################################################

# Python2 GET request with custom headers
url = 'https://google.com'

headers = {'User-Agent': "Googlebot"}

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print(response.read())
response.close()
