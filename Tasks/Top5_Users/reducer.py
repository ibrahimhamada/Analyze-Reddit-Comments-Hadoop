#!/usr/bin/python3

import sys
# sum all the values associated with keys to get the score of each subreddit
word = None
count = 0

for line in sys.stdin:
    key1,key2, value = line.strip().split()
    key=(key1,key2)
    if word is None: # runs first time the only in the loop
        word = key
    elif word != key:# if the key changes then push the line in the output and reset to get another key
        print(" ".join(word), value, sep='\t')
        word = key
print(" ".join(word), value, sep='\t')