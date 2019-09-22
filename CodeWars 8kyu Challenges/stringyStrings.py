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
'''

def stringy(size):
    #Initialize a list with size of 'size'
    num = [None] * size

    for i in range(0,size):

        #Also assign '1' to even-indexed elements, '0' to odd ones
        if i%2 == 0:
            num[i] = '1'
        else:
            num[i] = '0'

    #Return all elements of list as a string
    return "".join(num)


size = 6
print(stringy(size))
