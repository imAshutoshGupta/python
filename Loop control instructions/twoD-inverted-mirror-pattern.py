#   *****
#    ****
#     ***
#      **
#       *

s=0
for i in range(5,0,-1):
    for k in range(1,s+1):
        print("", end=" ")

    for j in range(1,i+1):
        print("*", end=" ")
    print()
    s=s+2

# for n input

n = int(input("enter the number: "))
s=0
for i in range(n,0,-1):
    for k in range(1,s+1):
        print("", end=" ")

    for j in range(1,i+1):
        print("*", end=" ")
    print()
    s=s+2
