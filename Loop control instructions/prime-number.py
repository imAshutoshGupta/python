# Prime number

n= int(input("enter number to check: "))

for i in range(2,n):
    r=n%i

    if r==0:
        print("non prime number")
        break
else:
    print("Prime Number")
                