'''
Written by: Orvin Demsy
Date: 19 August 2019

Write a function to split a string and convert it into an array of words. For example:

e.g:
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
'''

def string_to_array(s):
    return s.split(" ")

s = "I love you"

print(string_to_array(s))