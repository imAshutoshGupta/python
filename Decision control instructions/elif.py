x=int(input("enter value of x: "))
y=int(input("enter value of y: "))
z=int(input("enter value of z: "))

if (x>y) and (x>z):
    print("x is greater")
elif (y>x) and (y>z):
    print("y is greater")
elif (z>x) and (z>y):
    print("z is greater")