'''
Written by: Orvin Demsy
Date: 16 August 2019

Create a function that takes a string as an argument
and spit out that string in reverse

e.g:
hello -> olleh
'''

#The first method extended slice syntax
def reverse_word_1(word):
    return word[::-1] #Return olleH

print("The reversed input is = " + reverse_word_1(input("Enter a sentences/ a word : ")))

#The second method
def reverse_word_2(word):
    return ''.join(reversed(word))

print("The reversed input is = " + reverse_word_2(input("Enter a sentences/ a word : ")))

#Third method using loop
def reverse_word_3(word):
    str = ""
    for i in word:
        str = i + str
    return str

print("The reversed input is = " + reverse_word_3(input("Enter a sentences/ a word : ")))
