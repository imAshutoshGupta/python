# Calling a function in its own body is called as recursion
# Recursion is similar to never ending loop
'''
def greet()
    print("hello")
    greet()

greet()

loop repeats internally from line 6 to line 4

'''
#recursion
i=1
def greet ():
    global i
    print ("Hello-",i)
    i+=1
    greet ()
greet ()

# recursion error - maximum recursion depth exceeded

'''
In recursion every function call is preserved or stored in the memory
This builds a stack of memory. When that stack depth is exceeded or when that memory is filled with function calls then it generates recursion error.
As there is a condition to stop the loop there is also a condition written in the function body to stop the recursion.
To stop the recursion, return statement is used.
'''

print("----")

