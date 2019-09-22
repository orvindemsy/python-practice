'''
Written by: Orvin Demsy
Date: 17 August 2019

Source: https://coderbyte.com/solution/Letter%20Changes#Python

I'm rewriting it to get a better understanding

Challenge:
Have the function LetterCapitalize(str) take the str parameter being passed and
capitalize the first letter of each word. Words will be separated by only one space.

e.g.
Input:"hello world"
Output:"Hello World"


Input:"i ran there"
Output:"I Ran There"
'''


def LetterCapitalize(sentence):
    #Split the sentence into array of words
    word = sentence.split()
    for i in range(len(word)):
        #Create a word with first letter capitalized
        word[i] = word[i][0].upper() + word[i][1:]

    return " ".join(word)

sentence = "the man who can't be moved"
print(LetterCapitalize(sentence))