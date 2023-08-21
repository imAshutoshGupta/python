#division of two numbers
# error - when you put input as zero

n=int(input("Enter numerator: "))
d=int(input("enter denominator:     "))
div=n/d
print ("Division is: " , div)
print(type(div))


# using try-catch
try:    
    n=int(input("Enter numerator: "))
    d=int(input("enter denominator: "))
    div=n/d
    print ("Division is: " , div)         #python internally raises error and then the control is passed to the "except" block
    print(type(div))        

except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Please enter the value in digits only")

# cant type exceptions one by one, hence we use a universal exception (you cant give personalized messages tho)

try:    
    n=int(input("Enter numerator: "))
    d=int(input("enter denominator: "))
    div=n/d
    print ("Division is: " , div)        
    print(type(div))        

except Exception:
    print("Something went wrong!!!")

    # only technical definition of error

try:    
    n=int(input("Enter numerator: "))
    d=int(input("enter denominator: "))
    div=n/d
    print ("Division is: " , div)       
    print(type(div))        

except Exception as e:      #object
    print("Error: ",e)

