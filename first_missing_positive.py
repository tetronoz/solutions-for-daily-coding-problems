"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain 
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

items_1 = [3, 4, -1, 1]
items_2 = [1, 2, 0]

def first_missing_positive(items):
    l = len(items)

    if l == 0:
        return 1

    for i in range(l):
        if items[i] < 0:
            continue
        if items[i] >= l:
            continue
        if items[i] == items[items[i] - 1]:
            continue

        items[items[i]-1], items[i] = items[i], items[items[i]-1]
        i =- 1
    
    for i in range(l):
        if items[i] != i+1:
            return i + 1
    
    return l + 1

print(first_missing_positive(items_1))
print(first_missing_positive(items_2))