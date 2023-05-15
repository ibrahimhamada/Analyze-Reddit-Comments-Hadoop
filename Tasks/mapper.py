#!/usr/bin/python3

import sys
import json
# parse the line as json dictionary and print the subreddit as a key with weight equal to its upvotes + downvotes (high interaction)
for line in sys.stdin:
        key, value= line.split()
        user_subreddit=(value, key)
        print(" ".join(user_subreddit), 1 , sep='\t')