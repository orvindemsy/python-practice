'''
Written by: Orvin Demsy
Date: 18 August 2019

Re-learning the problem using the top solutino provided here
Source: https://coderbyte.com/editor/guest:Longest%20Word:Python#

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
  words = "".join([",", c][int(c.isalnum())] for c in sen).split(",")
  maxLen = max([len(w) for w in words])
  return [w for w in words if len(w) == maxLen][0]


sen = "fun&!! time"
print(LongestWord(sen))