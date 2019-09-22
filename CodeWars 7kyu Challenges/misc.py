'''
Written by: Orvin Demsy

Trying out new concepts/ functions.
'''

#Learn about enumerate
s1 = ['deer', 'goose', 'horse']
l1 = "geek"

#creating enumerate object
obj1 = enumerate(s1)
obj2 = enumerate(l1)

print ("Return type:",type(obj1))
print ("Enumerate l1 will result in: ", list(enumerate(l1)))
print ("Enumerate s1 will result in: ", list(enumerate(s1)))
print("\n")

#changing starting index to 2 from 0 (default)
print ("Enumerate l1 from 2 will result in: ", list(enumerate(l1, 2)))
print ("Enumerate s1 from 2 will result in: ", list(enumerate(s1, 2)))
print(" ")

#Using enumerate object in loops
for i in enumerate(s1):
    print (i)

print(" ")
for i, j in enumerate (l1,1):
    print (j)