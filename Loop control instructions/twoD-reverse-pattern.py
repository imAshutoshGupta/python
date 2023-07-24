#   Two D reverse star pattern

for i in range(5,0,-1):             #starts with zero, goes upto zero with "-1" decrement
    for j in range(1,i+1,1):
        print("*", end=" ")
    print()



#   For n number
n = int(input("enter your number: "))
for i in range(n,0,-1):     
    for j in range(1,i+1,1):
        print("*", end=" ")
    print()