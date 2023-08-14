# math module
# import modulename

import math
x = math.pi
print("value of pi:", x)
print("value of tau:", math.tau)

# alias -> import modulename as an alias

import math as m

x = m.factorial(5)  # m is the alias
print(x)

sqr = m.sqrt(16)
print(sqr)

# importing specific functionality from modules
# from modulename import function1, function2.....functionN

from math import factorial,sqrt
# x=math.factorial(5)  - error 
x = factorial(4)
print("factorial is:",x)

y = sqrt(4)
print("sqrt is:",y)
print(type(y))

from math import *  # will import only functions and stuff related to it

a = factorial(4)
print("factorial is:",a)

#importing strings

#string
import string
print ("Lower case:", string.ascii_lowercase) 
print ("Upper case:", string.ascii_uppercase)
print("digits:",string.digits)
x=string.ascii_lowercase+string.ascii_uppercase+string.digits
print (x)
print (x.upper())

# random module
# for random module generation

import random as r
x = r.random()
print()
y = x*10000
print(y)

otp = round(y)
print("OTP", otp)

# to prevent triple digit values we take range

otp = r.randrange(1000,10000)
print(otp)