#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    if len(words) == 3:
        try:
            if words[0] == '998' and:
                print'%s\t%s' % (words[1], words[2])
        except:
            continue