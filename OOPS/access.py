# Accessing methods via object
# objectname.methodname()

#method or function

class student:
    def greet(self):     # industry practice, can use any variable
        print("good afternoon")

#greet() # error: Undefined
# create object to access the class members
#objectname = classname()

s1=student()
s1.greet()  #python internally sends one object as greet(s1)
#^ obj.method()