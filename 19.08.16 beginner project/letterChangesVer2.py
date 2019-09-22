'''
Written by: Orvin Demsy
Date: 17 August 2019

Source: https://coderbyte.com/solution/Letter%20Changes#Python

I'm rewriting it to get a better understanding

Challenge :
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

e.g.
Input:"hello*3"
Output:"Ifmmp*3"


Input:"fun times!"
Output:"gvO Ujnft!"
'''



def LetterChanges(str):
    new_char = ""
    for char in str:
        #Checks if the character is alphabet
        if char.isalpha():
            #if the letter is z change it to a
            if char.lower() == 'z':
                char = "A"
            else:
                #if the letter is non-z
                #change it to the next character based on the order in ascii list
                char = chr(ord(char)+1)

                #capitlized the vowel
                if char in 'aiueo':
                    char = char.upper()

        #add the new character
        new_char = new_char + char

    return new_char

str = "hello!!"
print(LetterChanges(str))



