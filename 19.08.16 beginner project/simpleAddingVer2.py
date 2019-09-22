'''
Written by: Orvin Demsy
Date: 17 August 2019

Re-learning this solution for learning purposes
https://coderbyte.com/editor/guest:Simple%20Adding:Python

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
    return sum(range(1, num+1))

num = 1
print(simpleAdding(num))