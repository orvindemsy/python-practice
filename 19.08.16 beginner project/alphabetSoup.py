'''
Written by: Orvin Demsy
Date: 18 August 2019

Challenge:
Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the
letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation
symbols will not be included in the string.

Apparently my solution is the exact same as solution here
Source: https://coderbyte.com/solution/Alphabet%20Soup#Python
No need to re-learn

e.g.
Input:"coderbyte"
Output:"bcdeeorty"

Input:"hooplah"
Output:"ahhloop"
'''

def AlphabetSoup(string):
    string = list(string)
    string = sorted(string)
    return "".join(string)

string = input("Enter a word: ")
print(AlphabetSoup(string))