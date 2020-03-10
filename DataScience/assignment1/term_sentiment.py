import sys
import json

def build_sent_scores(sf):
    scores = {}
    for line in sf:
        term, score = line.split("\t")
        scores[term] = float(score)
    return scores

def build_tweet_scores(tf, ss):
    data = {}
    words = []

    i = 0
    for tweet in tf:
        data[i] = json.loads(tweet)
        total_score = 0.0

        for k,v in data[i].iteritems():
            if k == 'text':
                words = v.split(" ")
                for w in words[:]:
                    ew = w.encode('utf-8')
                    for x,y in ss.iteritems():
                        if x == ew:      
                            total_score += y
                for w in words[:]:
                    print w.encode('utf-8'), "{:4.3f}".format(total_score)
        i += 1

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file  = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ret = 0

    #lines(sent_file)
    #lines(tweet_file)

    sent_scores = {}
    sent_scores = build_sent_scores(sent_file)

    build_tweet_scores(tweet_file, sent_scores)

    tweet_file.close()
    sent_file.close()
        
if __name__ == '__main__':
    main()
