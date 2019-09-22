'''
Written by: Orvin Demsy
Date: 17 August 2019

This solution of mine is similar to the one provided online
https://coderbyte.com/solution/Simple%20Adding#Python

Challenge:
Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000.
Sample Test Cases

Sample output:
Input:12
Output:78

Input:140
Output:9870
'''

def simpleAdding(num):
    #declaring variable as total addition
    total = 0

    #generate num-iteration starting from 1
    for i in range(1, num+1):
        total = total + i

    return total

num = 4

print(simpleAdding(num))