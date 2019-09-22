'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
You get an array of numbers, return the sum of all of the positives ones.

Example
[1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.
'''


def positive_num(arr):
        return sum(list([x for x in arr if x > 0]))

arr = [-1, -2, 3, 4, 5]


print(arr)