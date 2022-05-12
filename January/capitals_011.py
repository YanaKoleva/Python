#!/usr/bin/env python3

import sys

def mid(s):
   return s[1:-1]


for line in sys.stdin:
   s = line.strip()
   middle = mid(s)
   if len(middle) > 0:
      m = str(s[0]).upper() + middle + str(s[-1]).upper()
      print(m)
   elif len(s) == 2:
      m = str(s[0]).upper() + str(s[-1]).upper()
      print(m)
