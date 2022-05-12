#!/usr/bin/env python3

import sys

list = [line.strip() for line in sys.stdin if len(line.strip()) > 4 if str(line.strip()) == str(line.strip)[::-1]]
print(list)
#for word in list:
