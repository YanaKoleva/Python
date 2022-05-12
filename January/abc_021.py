#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
num = lines[0].strip().split()
let = lines[1].strip()

a = min(int(num[0]), int(num[1]), int(num[2]))
c = max(int(num[0]), int(num[1]), int(num[2]))

d = {
   'A': str(a),
   'B': False,
   'C': str(c),
}
for k in num:
   if k != str(a) and k != str(c):
      for key in let:
         if key == 'B':
            d[key] = k
list = []
for key in let:
   list.append(d[key])
print(' '.join(list))
