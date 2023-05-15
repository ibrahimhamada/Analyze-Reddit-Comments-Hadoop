#!/usr/bin/python3

import sys

word = None
count = 0


for line in sys.stdin:
    key,value = line.strip().split()
    if word is None: 
        word = key
    elif word != key:
        print(" ".join(word), count, sep='\t')
        word = key
        count = 0
    count += int(value)

    
print(" ".join(word), count, sep='\t')