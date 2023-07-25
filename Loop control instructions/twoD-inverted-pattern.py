#  Inverted star pattern

#       Algorithm
#   Basic i loop
#   loop to print space
#   loop to print "*"

s=8
for i in range(1,6,1):              # i = number of stars in a line
    for k in range(1,s+1,1):
        print("", end=" ")
    for j in range(1,i+1,1):
        print("*", end=" ")
    print()
    s=s-2








