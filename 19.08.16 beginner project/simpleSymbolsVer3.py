'''
Re-learning the challenge using solution provided on the website for learning purposes
https://coderbyte.com/solution/Simple%20Symbols#Python

Written by: Orvin Demsy
Date: 17 August 2019

Challenge:
Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence
by either returning the string true or false. The str parameter will be composed of + and = symbols with several
characters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter.

e.g.
Input:"+d+=3=+s+"
Output:"true"


Input:"f++d+"
Output:"false"
'''


def simpleSymbols(string):

    string = "=" + string + "="

    for i in string:
        if i in "abcdefghijklmopqrstuvwxyz":
            if string[string.index(i)-1] != "+" or string[string.index(i)-1] != "+":
                return 'False'

    return 'True'


string = "+d+=3=+s+"
print(simpleSymbols(string))