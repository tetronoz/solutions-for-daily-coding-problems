"""
Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

intervals =  [(30, 75), (0, 50), (60, 150)]


def rooms_requried(intervals):
  intervals.sort()
  num = 0

  l = len(intervals)
  for i in range(l - 1):
    if intervals[i][1] > intervals[i+1][0]:
      num += 1

  if num == 0:
    return 1
  else:
    return num


print(rooms_requried(intervals))
