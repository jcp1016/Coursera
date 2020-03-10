import sys
import json

def build_scores(sf):
    scores = {}
    for line in sf:
        term, score = line.split("\t")
        scores[term] = float(score)
    return scores

def build_tweets(tf, ss):
    data = {}
    i,j = 0,0
    tot_score = 0.0
    words = []

    for tweet in tf:
        data[i] = json.loads(tweet)
        for k,v in data[i].iteritems():
            if k == 'text':
                words = v.split(" ")
                for w in words[:]:
                    ew = w.encode('utf-8')
                    for x,y in ss.iteritems():
                        if ew == x:      
                            tot_score += y
                print "{:4.3f}".format(tot_score)
                j += 1

        tot_score = 0
        if j == i:
            print "{:4.3f}".format(tot_score)
            j += 1
        i += 1

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file  = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #lines(sent_file)
    #lines(tweet_file)

    sent_scores = {}
    sent_scores = build_scores(sent_file)

    build_tweets(tweet_file, sent_scores)

    tweet_file.close()
    sent_file.close()
        
if __name__ == '__main__':
    main()
