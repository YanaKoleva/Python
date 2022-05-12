#!/usr/bin/env python3

import sys

b = []

for line in sys.stdin:
   line = line.strip().split(' ')
   b.append(line)

i = 0
a = int(b[0][0])
while i < len(b[1]):
  if a >= int(b[1][i]):
    a = a - int(b[1][i])
  else:
    break
  i = i + 1
print(i)
