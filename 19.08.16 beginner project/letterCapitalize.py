'''
Written by: Orvin Demsy
Date: 16 August 2019

Challenge:
Have the function LetterCapitalize(str) take the str parameter being passed and
capitalize the first letter of each word. Words will be separated by only one space.

e.g.
Input:"hello world"
Output:"Hello World"


Input:"i ran there"
Output:"I Ran There"
'''


def LetterCapitalize(words):
    #Use built in function to capitalize the first letter of each word
    new_words = words.title()
    return new_words


words = "i ran there"

print(LetterCapitalize(words))