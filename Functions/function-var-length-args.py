# variable length argument
#length of argument: number of arg in the function call is called as length of argument.

'''
def addition(x,y):
    z=x+y
    print(z)

addition(10,20)
addition(10)
addition(10,20,30)
'''

def addition(*x):
    print(x)
    print(type(x))

addition(10,20)
addition(10)
addition(10,20,30)


