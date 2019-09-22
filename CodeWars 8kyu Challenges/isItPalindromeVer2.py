'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.
Only one-word input is accepted

e.g.
madam = True
Mom = True
walter = False
'''

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = 'Mom'
print(is_palindrome(word))