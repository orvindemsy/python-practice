'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
In this simple exercise, you will create a program that will take two lists of integers, a and b.
Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b.
You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]),
the volume of a is 12 and the volume of b is 20.
Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code.
'''

def find_difference(a,b):
    #calculate the volum of a and b, and return the diff between them
    vol1 = 1
    vol2 = 1
    for i in a:
        vol1 = vol1 * i
    for j in b:
        vol2 = vol2 * j

    return abs(vol1-vol2)


a = [2, 3, 3]
b = [2, 3, 4]

print(find_difference(a, b))