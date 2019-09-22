'''
Written by: Orvin Demsy
Date: 18 August 2019

Challenge:
Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the
letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation
symbols will not be included in the string.

Re-learning the problem by solution provided here
Source: https://coderbyte.com/editor/guest:Alphabet%20Soup:Python

e.g.
Input:"coderbyte"
Output:"bcdeeorty"

Input:"hooplah"
Output:"ahhloop"
'''

def AlphabetSoup(string):

    return "".join(sorted(list(string)))

string = input("Enter a word: ")
print(AlphabetSoup(string))