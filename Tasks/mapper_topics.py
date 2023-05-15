#!/usr/bin/python3
import sys
import io
import re
import json
import nltk

top_users=["TweetPoster","autowikibot","PoliticBot","AutoModerator","[deleted]"]
top_subreddit=["AskReddit","leagueoflegends","funny" ,"nfl","pics"]
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
stop_words = set(stopwords.words('english'))


for line in sys.stdin:
        content=json.loads(line)
        score=content["score"]
        body = content['body']
        body = body.strip()
        body = re.sub(r'[^\w\s]', '',body)
        body = re.sub(r'\d+', '',body)
        body = body.lower()
        
        for x in body:
                if x in punctuations:
                        body=body.replace(x, " ") 
        topics = body.split()
        for topic in topics:
            if topic not in stop_words :
                 print("\t".join((topic,str(score))) )