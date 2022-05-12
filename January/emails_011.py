#!/usr/bin/env python3

import sys


def contains(s):
   for c in s:
      if str(c).isdigit():
         names = s[:s.find(c)]
         names = names.split('.')
         name = names[0][0].upper() + names[0][1:] + ' ' + names[1][0].upper() + names[1][1:]
         return name


for line in sys.stdin:
   line = line.strip()
   con = contains(line)
   print(con)
