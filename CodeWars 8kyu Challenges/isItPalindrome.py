'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.
Only one-word input is accepted

Self-evaluation:
After seeing the solution to this kata, this code is too inefficient

e.g.
madam = True
Mom = True
walter = False
'''

def is_palindrome(word):
    # if input is ''
    if word == None:
        return True

    #Counter to detect same character
    j = 0

    #Copy the word and create its reversed counterpart
    word1 = word
    word = list(word.lower())
    word1 = list(word1.lower())
    word.reverse()

    #Iterate and check each character
    for i in range(len(word)):
        if word[i] != word1[i]:
            j += 1
        else:
            j = j

    if j == 0:
        return True
    else:
        return False

word = 'ObgO'
print(is_palindrome(word))