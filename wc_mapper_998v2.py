#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    if len(words) == 4:
        try:
            if words[1] == '998' and words[2]:
                print '%s\t%s' % (words[1], words[2])
        except:
            continue
