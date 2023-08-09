#passing argument to function definition

#argument or parameter:
# the values passed to function definition from function call are called as argument or parameters.

#number of values passes to function = number of variables used to receive

def addition(x,y):
    z=x+y
    print("addition is: ",z)
    
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))

addition(a,b)

# for one arg (shows error)

def addition(x):
    z=x+y
    print("addition is: ",z)
    
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))

addition(a,b)

#for three arg (shows error)
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))

def addition(x,y,z):
    z=x+y
    print("addition is: ",z)
    
addition(a,b)