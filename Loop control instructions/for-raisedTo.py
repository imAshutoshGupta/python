n = int(input("enter number: "))
p = int(input("power you want to raise: "))

i=1
j=1
for i in range(1,0,-1):
    j*=n
print(j)