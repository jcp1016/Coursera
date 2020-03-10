import urllib2 as urllib
import sys
import json

_debug = 0

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

url = "https://api.github.com/users/mbostock/events"
encoded_post_data = None

opener = urllib.OpenerDirector()
opener.add_handler(http_handler)
opener.add_handler(https_handler)

url = "https://api.github.com/users/mbostock/events"
parameters = []
response = opener.open(url, encoded_post_data)

data = {}
i = 0

for line in response:
    data[i] = json.loads(line)
    print data[i]
