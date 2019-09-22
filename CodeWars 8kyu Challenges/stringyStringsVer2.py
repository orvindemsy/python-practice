'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
the string should start with a 1.
a string with size 6 should return :'101010'.
with size 4 should return : '1010'.
with size 12 should return : '101010101010'.
The size will always be positive and will only use whole numbers.

Try using top solutions:
source: https://www.codewars.com/kata/563b74ddd19a3ad462000054/solutions/python/all/best_practices
'''


def string(size):
    #This will replicate 10 (size/2)-times and putting 1 at the end when number is odd
    return "10" * (size/2) + "1" * (size % 2)

size = 6