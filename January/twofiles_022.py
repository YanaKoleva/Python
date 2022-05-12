#!/usr/bin/env python3


import sys

with open(sys.argv[1], 'r') as f:
   a_list = [line.strip() for line in f]

with open(sys.argv[2], 'r') as f:
   b_list = [line.strip() for line in f]

for (a, b) in zip(a_list, b_list):
   print(a)
   print(b)
