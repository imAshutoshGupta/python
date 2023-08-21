#division of two numbers
# error - when you put input as zero

n=int(input("Enter numerator: "))
d=int(input("enter denominator: "))
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