#find factorial of a number given by user

n = int(input("enter the number you want to factorial: "))

i=1
s=1
while i<=n:
    s=s*i
    i=i+1
print("Hence factorial of",n,"is",s)


# DRY RUN
#n=4
#i      i<=4        s=s*i       i=i+1

#i      i<=4        s=1         i=i+1=1+1
#i      i<=4        s=1*2       i=i+1=2+1
#i      i<=4        s=2*3       i=i+1=3+1
#i      i<=4        s=6*4       i=i+1=4+1
#i      i<=4        

print("   ")