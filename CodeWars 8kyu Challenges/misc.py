'''
Description:
To try out new function
'''

#Try lambda, map, filter
#source: https://www.geeksforgeeks.org/python-map-function/
from functools import reduce

a = [2, 3, 5, 4, 2]
b = 3
def add(n):
    return n + 20

c = lambda x : x + 20

lambda_filter = list(filter(lambda y: y <= 3, a))

lambda_map = list(map(lambda z: z*10, a))

lambda_reduce = reduce(lambda v, w: v*w, a )

sum_sum = sum(a)

#Various application of map
#print(sum_sum)
#source: https://www.geeksforgeeks.org/python-map-function/

def square(n):
    return n*n

def square2(x, y):
    return x * y

a1 = [2, 3, 4]
a2 = [5, 6, 7, 8]
a3 = ['set', 'cod', 'yuk', 'yah']

try1 = list(map(square, a))
try2 = list(map(square2, a1, a2))
try3 = list(map(list, a3))

print(try2)

#list comprehension
#source: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

try4 = []
for x in a1:
    for y in a2:
        if x != y:
            try4.append((x, y))

print(try4)


