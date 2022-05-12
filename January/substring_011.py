#!/usr/bin/env python3

import sys

a = []

for line in sys.stdin:
   s = line.strip()
   a.append(s.split(" "))

i = 0
while i < len(a):
   if str(a[i][0]).lower() in str(a[i][1]).lower():
      print("True")
   else:
      print("False")
   i = i + 1
