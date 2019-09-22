'''
Written by: Orvin Demsy
Date: 16 August 2019

Challenge :
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm.
Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

e.g.
Input:"hello*3"
Output:"Ifmmp*3"


Input:"fun times!"
Output:"gvO Ujnft!"

All capitalized letter will be lower-cased
'''

import string
alphabet = string.ascii_lowercase
alphabet = list(alphabet)

word = input("Enter a sentence or words : ")
word = word.lower()
new_word = ""

for i in range(len(word)):
    #check if the character is alphabet
    if word[i].isalpha():
        #check if the character is z
        if word[i] == "z":
            new_word = new_word + "A"
        #check if the character is not z
        elif word[i] != "z":
            new_idx = alphabet.index(word[i]) + 1
            #check if the new character is alphabet
            if alphabet[new_idx].lower() in "aiueo":
                new_word = new_word + alphabet[new_idx].upper()
            else:
            #check if the new character is not alphabet
                new_word = new_word + alphabet[new_idx]
    #check if the character is not alphabet
    else:
        new_word = new_word + word[i]



print(new_word)
