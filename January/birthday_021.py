#!/usr/bin/env python3


import sys

import calendar

d = {
   0: "Monday",
   1: "Tuesday",
   2: "Wednesday",
   3: "Thursday",
   4: "Friday",
   5: "Saturday",
   6: "Sunday",
}

text = {
   0: "Monday's child is fair of face.",
   1: "Tuesday's child is full of grace.",
   2: "Wednesday's child is full of woe.",
   3: "Thursday's child has far to go.",
   4: "Friday's child is loving and giving.",
   5: "Saturday's child works hard for a living.",
   6: "Sunday's child is fair and wise and good in every way.",
}

for line in sys.stdin:
   line = line.strip().split()
   day = int(line[0])
   month = int(line[1])
   year = int(line[2])
   dayy = calendar.weekday(year, month, day)
   if dayy in d:
      m = d[dayy]
      if dayy in text:
         print("You were born on a " + m + " and " + text[dayy])
