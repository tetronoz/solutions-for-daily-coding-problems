"""
Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

#
# Idea - http://blog.gainlo.co/index.php/2016/07/12/meeting-room-scheduling-problem/
# Impelementation - https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_21_25.py
#

def rooms_required_bruteforce(intervals):
    l = len(intervals)

    if l == 0 or l == 1:
        return l

    intervals.sort()

    max_rooms = 0

    for i in range(l-1):
        nums = 1
        for j in range(i+1, l):
            if intervals[i][1] >= intervals[j][0]:
                nums += 1
                max_rooms = max(nums, max_rooms)

    return max_rooms

def rooms_required(intervals):
    l = len(intervals)

    if l == 0 or l == 1:
        return l

    starts = [(el[0],1) for el in intervals]
    ends = [(el[1],-1) for el in intervals]
    starts_ends = [e[1] for e in sorted(starts + ends, key=lambda e: e[0])]

    rooms = 0
    events = 0
    for event in starts_ends:
        events += event
        rooms = max(rooms, events)

    return rooms


assert rooms_required_bruteforce([]) == 0
assert rooms_required_bruteforce([(30, 75), (0, 50), (60, 150)]) == 2
assert rooms_required_bruteforce([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert rooms_required_bruteforce([(60, 150)]) == 1
assert rooms_required_bruteforce([(60, 150), (150, 170)]) == 2
assert rooms_required_bruteforce([(60, 150), (60, 150), (150, 170)]) == 3


assert rooms_required([]) == 0
assert rooms_required([(30, 75), (0, 50), (60, 150)]) == 2
assert rooms_required([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert rooms_required([(60, 150)]) == 1
assert rooms_required([(60, 150), (150, 170)]) == 2
assert rooms_required([(60, 150), (60, 150), (150, 170)]) == 3
