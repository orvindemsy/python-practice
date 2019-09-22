'''
Written by: Orvin Demsy
Date: 16 August 2019

I'm curious how slicing works, so I tried out different combination


H   e  l  l  o
0   1  2  3  4
-5 -4 -3 -2 -1
'''

def reverse_word_1(word):
    return word[::-1] #Return olleH

def reverse_word_2(word):
    return word[0::-1] #Return H

def reverse_word_3(word):
    return word[0::] #Return Hello

def reverse_word_4(word):
    return word[:len(word)] #Return Hello

def reverse_word_5(word):
    return word[:len(word):-1] #Return ''

def reverse_word_6(word):
    return word[0:len(word)] #Return Hello

def reverse_word_7(word):
    return word[0:len(word):-1] #Return ''

def reverse_word_8(word):
    return word[-2:] #Return lo

def reverse_word_9(word):
    return word[:-2] #Return Hel

def reverse_word_10(word):
    #return word[:1:-1] #Return ?
    #return word[:-3:-1] #Return ?
    return word[-3::-1] #Return ?

print("reverse word_1 = " + reverse_word_1("Hello"))

print("reverse word_2 = " + reverse_word_2("Hello"))

print("reverse word_3 = " + reverse_word_3("Hello"))

print("reverse word_4 = " + reverse_word_4("Hello"))

print("reverse word_5 = " + reverse_word_5("Hello"))

print("reverse word_6 = " + reverse_word_6("Hello"))

print("reverse word_7 = " + reverse_word_7("Hello"))

print("reverse word_8 = " + reverse_word_8("Hello"))

print("reverse word_9 = " + reverse_word_9("Hello"))

print("reverse word_10 = " + reverse_word_10("Hello"))