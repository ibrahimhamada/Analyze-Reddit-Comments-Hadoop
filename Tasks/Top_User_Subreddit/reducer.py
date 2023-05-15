#!/usr/bin/python3

import sys

word = None
count = 0


for line in sys.stdin:
    username, subreddit, value = line.strip().split()
    key=(username,subreddit)
    if word is None:
        word = key
    elif word != key:
        print(" ".join(word), '\t',count)
        word = key
        count = 0
    count += int(value)

    
print(" ".join(word), '\t',count)
