#!/usr/bin/python3

# This is the reducer script, which accumulates                                   #
# The reducer should expect the following:                                        #
# (Subreddit_id, subreddit_name, topic, accumulative_commentt_count,              #
# accumulative_score,  accumulative_controversiality)                             #
# Where, the key is the (subreddit, topic)                                        #
# -------------------------------------------                                     #
# The output data from this map-reduce job is the basis for all remaining jobs    #
# , since it's been cleaned from issues found in the RAW data                     #

import sys

sub_id = None
sub_name = None
count = 0


for line in sys.stdin:
    next_sub_id, next_sub_name, next_count = line.strip().split()
    next_count = int(next_count)
    if sub_id is None:
        sub_id = next_sub_id
        sub_name = next_sub_name
    elif sub_id != next_sub_id:
        print(sub_id, next_sub_name, count, sep='\t')
        sub_id = next_sub_id
        sub_name = next_sub_name
        count = 0
    count += next_count
print(sub_id, sub_name, count, sep='\t')
