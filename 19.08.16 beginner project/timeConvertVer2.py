'''
Written by: Orvin Demsy
Date: 17 August 2019

Re-writing the solution provided online for learning purposes
https://coderbyte.com/editor/guest:Time%20Convert:Python

Challenge:
Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes
the parameter converts to (ie. if num = 63 then the output should be 1:3).
Separate the number of hours and minutes with a colon.

Sample Test Cases:
Input:126
Output:"2:6"

Input:45
Output:"0:45"
'''

def TimeConvert(num):
    #The // operator divides the dividend tjen return the integer value of quotient.
    hour = num // 60
    min = num - (hour * 60)
    return ":".join([str(hour), str(min)])


num = input("Enter the number of minute(s): ")
print(TimeConvert(int(num)))
