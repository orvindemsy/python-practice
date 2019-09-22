'''
Written by: Orvin Demsy
Date: 17 August 2019

My solution is similar to the following solution
https://coderbyte.com/solution/Time%20Convert#Python

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
    #Use division and modulo operator
    hour = int(num / 60)
    min = int(num % 60)

    #Convert the hour and min into string
    return (str(hour) + ":" + str(min))

#Print the result
num = input("Enter the number of minute(s): ")
print(TimeConvert(int(num)))
