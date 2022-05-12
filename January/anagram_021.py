#!/usr/bin/env python3

import sys

def isanagram(a, b):
   for c in a:
      if c not in b:
         return False
      b = b.replace(c, '', 1)
   if len(b) == 0:
      return True
   else:
      return False


for line in sys.stdin:
   line = line.strip().split()
   print(isanagram(line[0], line[1]))
