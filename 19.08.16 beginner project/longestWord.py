'''
Written by: Orvin Demsy
Date: 18 August 2019

I can't solve this problem on my own
so use the solution provided
Source: https://coderbyte.com/solution/Longest%20Word#Python

Note to myself:
I didn't know about maketrans and translate built-in function. I took me hours just trying to figure out how to
strip off the punctuation marks

Challenge :
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty. Using

e.g.
Input:"fun&!! time"
Output:"time"

Input:"I love dogs"
Output:"love"
'''
import string

def LongestWord(sen):
# first we remove non alphanumeric characters from the string
  # using the translate function which deletes the specified characters
  word = sen.maketrans("","", "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")

  sen = sen.translate(word)

  # now we separate the string into a list of words
  arr = sen.split(" ")

  # the list max function will return the element in arr
  # with the longest length because we specify key=len
  return max(arr, key=len)


sen = "fun&!! time"
print(LongestWord(sen))