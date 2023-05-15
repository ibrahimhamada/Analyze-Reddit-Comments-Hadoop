#!/usr/bin/python3

import sys
import json
# parse the line as json dictionary and print the subreddit as a key with weight equal to its upvotes + downvotes (high interaction)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for line in sys.stdin:
        for x in line:
                if x in punctuations:
                        line=line.replace(x, " ") 
        key, value,a = line.strip().split()
        user_subreddit=(a, key,value)
        print(" ".join(user_subreddit) , sep='\t')