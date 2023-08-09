#function with no argument and no return value

# Working of a function.
# When a function call is detected control goes to function body, it executes function body and return control at a place of function call thus completing the cycle.

def addition():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    c=a+b
    print("addition is c: ",c)

addition() #call to function
print("after first function call")
addition()