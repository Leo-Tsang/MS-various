#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if len(line) >=2:
        word = line[0]
        count = line[1]

        print '%s\t%s' % (word, count)
