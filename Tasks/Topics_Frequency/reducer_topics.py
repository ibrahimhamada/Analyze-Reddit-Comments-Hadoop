#!/usr/bin/python3

import sys

word = None
count = 0


for line in sys.stdin:
    topic,user, subreddit, value = line.strip().split()
    if word is None: 
        word = (topic,user,subreddit)
    elif word != (topic,subreddit):
        print(word, count, sep='\t')
        word = (topic,user,subreddit)
        count = 0
    count += int(value)

    
print(" ".join(word), count, sep='\t')