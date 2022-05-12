#!/usr/bin/env python3

import sys

def long(s):
   from math import pi
   return f'{pi:.{s}f}'


for line in sys.stdin:
   line = line.strip()
   print(long(line))
