#!/usr/bin/python3

# This script maps the RAW json file format into                                  #
# (Subreddit_id, subreddit_name, topic, accumulative_commentt_count,              #
# accumulative_score)                             #
# Where, the key is the (subreddit, topic)                                        #
# --------------------------------------------                                    #
# As such, it tries to infer the topic from the comment. We will assume that      #
# the most frequent noun reflects the topic of the comment.                       #
# -------------------------------------------                                     #
# The output data from this map-reduce job is the basis for all remaining jobs    #
# , since it's been cleaned from issues found in the RAW data                     #

import sys
import json
import re
from datetime import datetime


def check_flawed(json_obj:dict)-> str:
    ''' checks if the json_object is corrupted or the comment is flawed, discarding flawed comments
    Returns a cleaned version of the comment body
    '''

    # check json_object integrity
    attributes = set(["body", "subreddit_id", "subreddit", "score", "created_utc"])
    if not attributes.issubset(json_obj.keys()):
        raise ValueError("JSON object doesn't have the important attributes")
    
    # remove non-Enlgish unicode characters
    body = json_obj["body"].encode("ascii", errors="ignore").strip().decode("ascii")
    ts = int(json_obj["created_utc"])
    year = datetime.utcfromtimestamp(ts).strftime('%m')
    return body, year


def extract_words(body:str):
    '''
    Tries the get the count of words we're interested in
    '''
    # list of words we're interested in
    fuck = re.findall("[fF]+[uU]+[cC]+[kK]+", body)
    bitch = re.findall("[bB]+[iI]+[tT]+[cC]+[hH]+", body)
    bastard = re.findall("[bB]+[aA]+[sS]+[tT]+[aA]+[rR]+[dD]+", body)
    shit = re.findall("[sS]+[hH]+[iI]+[tT]+", body)

    return len(fuck) + len(bitch) + len(bastard) + len(shit)


for line in sys.stdin:
    line = line.strip()
    # try to convert to json object
    try:
        json_obj = json.loads(line)
        # check for flaws and clean 
        ascii_body, year = check_flawed(json_obj)
        # get topic
        curse_sum = extract_words(ascii_body)
        # print
        print(json_obj["subreddit_id"], json_obj["subreddit"], curse_sum, sep="\t")

    except ValueError as e:
        pass