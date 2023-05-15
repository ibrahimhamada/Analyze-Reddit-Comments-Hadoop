#!/usr/bin/python3

import sys

def Parser():
    for line in sys.stdin:
        line = line.strip('\n')
        yield line.split("\t")


counts = list(Parser())
z = sorted(counts, key = lambda x: int(x[1]))[:5]
print('\n'.join(map(lambda x: '\t'.join(x), z)))
