#!/usr/bin/env python3

import sys

def isanagram(a):
   b = []
   a = a.strip().lower()
   for c in a:
      if c.isalnum():
         b.append(c)
   return b == b[::-1]


for line in sys.stdin:
   print(isanagram(line))
