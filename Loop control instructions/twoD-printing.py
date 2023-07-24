# Two-D pattern printing

#   DRY RUN
#
#   i=1         *           i=1
#   i=2         **          j=1,2
#   i=3         ***         j=1,2,3
#   i=4         ****        j=1,2,3,4
#   i=5         *****       j=1,2,3,4,5


for i in range(1,13,1):
    for j in range(1,i+1,1):
        print(i, end=" ")
    print()


for i in range(1,13,1):
    for j in range(1,i+1,1):
        print("*", end=" ")
    print()