#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = int(line.strip())
    if line %2 == 0:
        print '%s\t%s' % ("even", 1)
    else:
        print '%s\t%s' % ("odd", 1)