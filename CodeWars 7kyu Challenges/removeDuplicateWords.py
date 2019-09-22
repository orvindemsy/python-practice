'''
Written by: Orvin Demsy
Date: 21 Aug 2019

Description:
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:
'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:
'alpha beta gamma delta'
'''

string = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

def remove_duplicate_words(string):
    new = []
    string = string.split(" ")
    [new.append(s) for s in string if s not in new]
    return ' '.join(new)

print(remove_duplicate_words(string))
