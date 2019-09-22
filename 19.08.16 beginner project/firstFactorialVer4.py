'''
Written by: Orvin Demsy
Date: 17 August 2019

Re-learning the solution here https://coderbyte.com/editor/guest:First%20Factorial:Python

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

    if num == 1:
        return 1
    else:
        return num * firstFactorial(num-1)


num = 4
print(firstFactorial(num))