'''
Written by: Orvin Demsy

CodeWars Challenge
https://www.codewars.com/kata/mumbling/train/python

Date: 21 August 2019

Create a system that fulfills the following inputs and outputs
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

string = "RqaEzty"
new = []


def mumbling(string):
    string = list(string)

    for i in range(len(string)):
        new.append((string[i] * (i + 1)))

    for i in range(len(new)):
        new[i] = new[i].capitalize()

    return "-".join(new)


print(mumbling(string))

