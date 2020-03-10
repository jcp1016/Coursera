import sys
import json

def build_scores(sf):
    scores = {}
    for line in sf:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def build_tweets(tf, ss):
    data = {}
    words = []
    i, tot_score = 0,0
    country = ''
    state_name = ''
    state_scores = {}

    for tweet in tf:
        data[i] = json.loads(tweet)
        for k,v in data[i].iteritems():
            if k == 'place' and v <> None:
                country = data[i]['place']['country'].encode('utf-8')
                state_name = data[i]['place']['full_name'].encode('utf-8')[-2:]

            if k == 'text':
                words = v.split(" ")
                for w in words[:]:
                    ew = w.encode('utf-8')
                    for x,y in ss.iteritems():
                        if ew == x:      
                            tot_score += y

        if country == 'United States' and state_name <> 'US':
            if state_name in state_scores:
                state_scores[state_name] += tot_score
            else:
                state_scores[state_name] = tot_score

        i += 1
        tot_score = 0
        country = ""
        state_name = ""

    l = sorted(state_scores.items(), key=lambda x:x[1], reverse=True)
    print l[0][0]

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
