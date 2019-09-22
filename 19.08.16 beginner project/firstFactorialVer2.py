'''
Written by: Orvin Demsy
Date: 17 August 2019

Challenge:
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Sample Test Cases. WITHOUT USING MATH FUNCTION!

e.g.:
Input:4
Output:24

Input:8
Output:40320
'''

def firstFactorial(num):
    #initial declaration of variable total as total of factorial
    total = 1

    #exception if the input number is 1
    if num == 1:
        total = 1

    #if the input number isn't 1
    else:
        #iterating num times, starting from zero
        for i in range(num):
            total = total * num
            #decreasing num each iteration
            num = num - 1

    return total

num = 2
print(firstFactorial(num))