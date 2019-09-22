'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
If you can't sleep, just count sheep!!
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
Input will always be valid, i.e. no negative integers.

e.g.
n = 2
output = "1 sheep...2 sheep..."

n = 3
output = "1 sheep...2 sheep...3 sheep..."
'''

#convert the single integer to range of value from 1 to n
#convert the value of list of int to str
#combine them with " sheep..."

def count_sheep(n):
    return " sheep...".join(str(num) for num in list(range(1, n+1))) + " sheep..."

n = 3
print(count_sheep(n))