"""
Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def rooms_requried(intervals):
  starts = [(el[0],1) for el in intervals]
  ends = [(el[1],-1) for el in intervals]
  starts_ends = [e[1] for e in sorted(starts + ends, key=lambda e: e[0])]

  rooms = 0
  events = 0
  for event in starts_ends:
    events += event
    rooms = max(rooms, events)

  return rooms


assert rooms_requried([]) == 0
assert rooms_requried([(30, 75), (0, 50), (60, 150)]) == 2
assert rooms_requried([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert rooms_requried([(60, 150)]) == 1
assert rooms_requried([(60, 150), (150, 170)]) == 2
assert rooms_requried([(60, 150), (60, 150), (150, 170)]) == 3
