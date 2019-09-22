'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.
Goodluck :)

e.g.
input = 1
output = 1

input = 111
output = 121

input = 9999
output = 10000
'''

#sq num
#1 4 9 16 25 36 49 64 81 100 121 144 169 196 225

'''
1 1
2 1
3 4
4 4
5 4
6 4
7 9
8 9
10 9


'''
import math

#Find the square root of n, round it, and square that number
def nearest_sq(n):
    return round(math.sqrt(n))**2

n = 111

print(nearest_sq(n))
