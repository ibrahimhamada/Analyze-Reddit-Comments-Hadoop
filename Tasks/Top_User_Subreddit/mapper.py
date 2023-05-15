#!/usr/bin/python3
top_subreddit=["AskReddit","leagueoflegends","funny" ,"nfl","pics"]
import sys
import json

for line in sys.stdin:
        content=json.loads(line)
        
        if content['subreddit'] in top_subreddit:
           user_subreddit=(content['author'],content['subreddit'])
           print(" ".join(user_subreddit), 1,sep="\t" )