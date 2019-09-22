'''
Written by: Orvin Demsy
Date: 21 August 2019

CodeWars Challenge
https://www.codewars.com/kata/mumbling/train/python

Re-learning using the solution providede online:
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/solutions/python

Date: 18 August 2019

Create a system that fulfills the following inputs and outputs
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

string = "RqaEzty"
new = []


def mumbling(string):
    return '-'.join(c.capitalize() + c.lower() * i for i,c in enumerate(string))

print(mumbling(string))

