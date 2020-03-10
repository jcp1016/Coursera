import urllib
import json

j = 1
for k in range(1,10):
    myurl = "http://search.twitter.com/search.json?q=goldman sachs&page=" + str(k)
    response = urllib.urlopen(myurl)

    pyresponse = json.load(response)
    results = pyresponse["results"]

    for i in range(10):
        if results[i]["iso_language_code"] == "en":
            print str(j) + ") " + results[i]["text"]
            j += 1
