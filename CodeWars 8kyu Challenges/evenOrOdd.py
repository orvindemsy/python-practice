'''
Written by: Orvin Demsy
Date: 19 August 2019

Description:
Create a function (or write a script in Shell)
that takes an integer as an argument and returns
"Even" for even numbers or "Odd" for odd numbers.

e.g.:
input 2 => 'Even'
input 0 => 'Even'
input 9 => 'Odd'
input -1 => 'Odd'
input 100 => 'Even'
'''
'''
def even_or_odd(number):
    return 'Even' if number%2 == 0 else 'Odd'

#print(even_or_odd(100))
n = 2

if n%2:
    print('odd')
else:
    print('even')
'''

mytxt = '12345678'

print(mytxt[-2:])