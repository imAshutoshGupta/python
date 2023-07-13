#find factorial of a number given by user

n = int(input("enter the number you want to factorial: "))

i=1
s=1
while i<=n:
    s=s*i
    i=i+1
print("Hence factorial of",n,"is",s)
