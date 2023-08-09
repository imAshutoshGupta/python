'''
Types of arguments:
1) Positional argument
2) Default argument
3) Variable length argument

Default argument:
The argument in the function definition has a default value.
If the value is provided by function call, it will override the given value.
If not, default value of argument is taken

'''

def addition(x=0,y=0):
    print(x)
    print(y)
    z=x+y
    print("addition is: ",z)

addition(10,20)
addition(15)
addition()