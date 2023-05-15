#!/usr/bin/python3

import sys
import json

for line in sys.stdin:
        content=json.loads(line)
        print(content['author'], 1 , sep='\t')