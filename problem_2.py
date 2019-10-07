"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]

Follow-up: what if you can't use division?
"""

from functools import reduce

ar_1 = [1, 2, 3, 4, 5]
ar_2 = [3, 2, 1]
def product_of_all_except_i(ar):
    new_ar = []
    ar_prod = reduce(lambda x, y: x*y, ar)
    for val in ar:
        new_ar.append(ar_prod // val)
    
    return new_ar

print("With division")
print(product_of_all_except_i(ar_1))
print(product_of_all_except_i(ar_2))

def product_of_all_except_i_no_div(ar):
    l = len(ar)
    new_ar = []
    for i in range(l):
        if i == 0:
            p = reduce(lambda x,y: x*y, ar[i+1:])
            new_ar.append(p)
        elif i == l:
            p = reduce(lambda x, y: x*y, ar[:i])
            new_ar.append(p)
        else:
            temp = ar[0:i] + ar[i+1:]
            p = reduce(lambda x,y: x*y, temp)
            new_ar.append(p)
    
    return new_ar

print()
print("No division")

print(product_of_all_except_i_no_div(ar_1))
print(product_of_all_except_i_no_div(ar_2))
