import sys
import json

def top_ten_hashtags(tf):
    data = {}
    hashtags = [{}]
    hashtag_ct = {}
    t = ""

    i = 0
    for tweet in tf:
        data[i] = json.loads(tweet)

        for k in data[i].iterkeys():
            if k == 'entities':
                for x,y in data[i]['entities'].iteritems():
                    if x == 'hashtags':
                        for ht in data[i]['entities']['hashtags']:
                            t = ht['text'].encode('utf-8')
                            if t in hashtag_ct:
                                hashtag_ct[t] += 1
                            else:
                                hashtag_ct[t] = 1  
        i += 1
        t = ""

    l = sorted(hashtag_ct.items(), key=lambda x:x[1], reverse=True)
    for i in range(10):
        print l[i][0], "{:4.1f}".format(l[i][1])

def main():
    tweet_file = open(sys.argv[1])

    top_ten_hashtags(tweet_file)

    tweet_file.close()
        
if __name__ == '__main__':
    main()
