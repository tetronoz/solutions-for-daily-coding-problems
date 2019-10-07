"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
"""

ar = [10, 15, 3, 7]
k = 17
match = {}

def sum_of_two(ar, k):
    for val in ar:
        if val in match:
            return True
        else:
            match[k-val] = val
    return False

print(sum_of_two(ar, k))