import sys
import json

def compute_freqs(tf):
    data = {}
    words = []
    all_terms_count = 0.0
    terms = {}
    term_freq = {}

    i = 0
    for tweet in tf:
        data[i] = json.loads(tweet)
        for k,v in data[i].iteritems():
            if k == 'text':
                words = v.split(" ")
                words = filter(bool, words)
                for w in words[:]:
                    if w <> None:
                        all_terms_count += 1.0
                        ew = w.encode('utf-8')
                        term_found = 0
                        for x,y in terms.iteritems():
                            if x == ew:
                                terms[ew] += 1.0
                                term_found = 1
                        if term_found == 0:
                            terms[ew] = 1.0
        i += 1
    if all_terms_count > 0:
        for k,v in terms.iteritems():
            term_freq[k] = v/all_terms_count
            print k.strip('\r\n') + " " + "{:1.4f}".format(v/all_terms_count)

def main():
    tweet_file = open(sys.argv[1])

    compute_freqs(tweet_file)

    tweet_file.close()
        
if __name__ == '__main__':
    main()
