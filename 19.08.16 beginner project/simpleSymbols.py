'''
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

import string

#generate a list of array full of alphabet
alpha = string.ascii_lowercase
string1 = "+d+=3=+s+" #should return true
string2 = "f++d+"     #should return false
check = []

def SimpleSymbols(string):
    #surround the string with "=" to prevent character
    #appearing as the first of letter of the word generates
    #error or anomaly
    string = "=" + string + "="

    #convert string into list
    char = list(string)
    #j is used as true or false parameter
    j = 0

    # iterate each character in string and put it into char[i
    for i in range(len(string)):

        #check whether the char contains alphabet
        if char[i] in alpha:

            #check whether the alphabet is padded by "+"
            if char[i + 1] and char[i - 1] == "+":
                j = j
            else:
                j += 1

    #if j is 0, the string fulfills the requirements
    if j == 0:
        isTrue = True

    # if j is 1, the string doesn't fulfill the requirements
    else:
        isTrue = False

    #return the value
    return isTrue

# keep this function call here

print(SimpleSymbols(string2))