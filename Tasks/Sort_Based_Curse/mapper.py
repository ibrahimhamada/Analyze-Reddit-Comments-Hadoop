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
import heapq

sub_id = None
sub_name = None

top_10 = []
[heapq.heappush(top_10, (-1, "dummy_id","dummy_subreddit")) for _ in range(10)]

for line in sys.stdin:
    sub_id, sub_name, count = line.strip().split()
    count = int(count)
    heapq.heappushpop(top_10, (count, sub_id, sub_name))

top_10_rev = []
for _ in range(len(top_10)):
    count, sub_id, sub_name = heapq.heappop(top_10)
    if sub_id != "dummy_id":
        top_10_rev.append((sub_id, sub_name, count))

top_10_rev = top_10_rev[::-1]
for top in top_10_rev:
    sub_id, sub_name, count = top
    print(sub_id, sub_name, count, sep="\t")