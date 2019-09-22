'''
Written by: Orvin Demsy
Date: 19 August 2019

Some new animals have arrived at the zoo.
The zoo keeper is concerned that perhaps the animals do not have the right tails.
To help her, you must correct the broken function to make sure that the second argument (tail),
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.
The arguments will always be strings, and normal letters.

For Haskell, body has the type of String and tail has the type of Char.
For Go, body has type string and tail has type rune.

e.g:
Fox -> x, True
Rhino -> o, True
Badger -> y, False
'''

def correct_tail(body, tail):
    return body[-1] == tail

body = "Fox"
tail = "x"

print(correct_tail(body, tail))