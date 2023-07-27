#WAP to find one number raised to power.

n = int(input("enter number"))
p =  int(input("enter the power"))

i=1
t=1
while i<=p:
    t=t*n
    i=i+1
print("result: ", t)