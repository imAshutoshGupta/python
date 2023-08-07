#multidimensional list
l = [[11,9,7],[1,-2,5],[9,5,6]]
print("entire nested list: ", l)
print("list first element: ", l[0])
print("list second element: ", l[1])
print("list third element: ", l[2])


# accessing each value (like a matrix)

print("First row elements: ")
print(l[0][0])
print(l[0][1])      #i=0 j=0,1,2
print(l[0][2])

print("Second row elements: ")
print(l[1][0])
print(l[1][1])      #i=1 j=0,1,2
print(l[1][2])

print("Third row elements: ")
print(l[2][0])
print(l[2][1])      #i=2 j=0,1,2
print(l[2][2])


# accessing using loops 

            
# #dry run
# i     j

# 0     0
#       1
#       2

# 1     0
#       1
#       2

# 2     0
#       1
#       2

for i in range(0,3,1):
    for j in range(0,3,1):
        print(l[i][j])

















