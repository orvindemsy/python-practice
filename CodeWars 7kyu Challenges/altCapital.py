'''
Written by: Orvin Demsy

CodeWars Challenge
https://www.codewars.com/kata/alternate-capitalization/train/python


Date: 23 August 2019

Create a system that fulfills the following inputs and outputs
Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
Return it as a list instead of tuple
'''

def altCapital(s):
    word1 = ""
    word2 = ""
    word1 = ''.join(word1 + s[i].upper() if not i % 2 else word1 + s[i] for i, c in enumerate(s))
    word2 = ''.join(word2 + s[i].upper() if i % 2 else word2 + s[i] for i, c in enumerate(s))
    return [word1,word2]

#new = ""
s = "abcdef"


print(altCapital(s))