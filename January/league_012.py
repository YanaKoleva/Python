#!/usr/bin/env python3

import sys

top = ['POS', 'CLUB', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS']

def main():
   lines = []
   for line in sys.stdin:
      lines.append(line.strip().split())
   c = []
   for line in lines:
      c.append(' '.join(line[1:-8]))
   longest = 0
   for a in c:
      if longest < len(a):
         longest = len(a)

   print(f'{top[0]:>3s} {top[1]:{longest:d}s} {top[2]:>2s} {top[3]:>3s} '
         f'{top[4]:>3s} {top[5]:>3s} {top[6]:>3s} {top[7]:>3s} {top[8]:>3s} {top[9]:>3s}')

   for line in lines:
      pos = int(line[0])
      club = ' '.join(line[1:-8])
      p = int(line[-8])
      w = int(line[-7])
      d = int(line[-6])
      lost = int(line[-5])
      gf = int(line[-4])
      ga = int(line[-3])
      gd = int(line[-2])
      pts = int(line[-1])
      print(f'{pos:3d} {club:{longest:d}s} {p:2d} {w:3d}'
            f'{d:4d} {lost:3d} {gf:3d} {ga:3d} {gd:3d} {pts:3d}')


if __name__ == '__main__':
    main()
