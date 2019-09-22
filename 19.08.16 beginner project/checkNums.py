'''
Written by: Orvin Demsy
Date: 17 August 2019

The solution provided online more or less similar to my solution
https://coderbyte.com/editor/guest:Time%20Convert:Python
https://coderbyte.com/solution/Check%20Nums#Python

Challenge
Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.
Sample Test Cases

Input:3 & num2 = 122
Output:"true"


Input:67 & num2 = 67
Output:"-1"
'''

def CheckNums(num1,num2):

    if num2 > num1:
        return 'true'
    elif num1 > num2:
        return 'false'
    else:
        return '-1'

num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
print(CheckNums(num1, num2))
