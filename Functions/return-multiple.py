# return statement in python can return multiple values in python

# returning multiple values

#returning multiple values
def arithmetic (a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add, sub, mul, div

x,y,z,d=arithmetic (9, 2) #add, sub, mul, div
print ("Addition is:",x)
print ("Subtraction is:",y)
print("Multiplication is:",z)
print ("Division is:",d)