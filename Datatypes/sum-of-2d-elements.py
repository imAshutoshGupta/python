#WAP to find the sum of elements in a two dimensional list

l = [5,6,7],[3,5,8],[7,5,3]
s = 0
for i in range(0,3):
    for j in range(0,3):
        print(l[i][j],end="")
        s = s+l[i][j]
    print()
print("summation is:" , s)

'''
Dry run
i   j   l[i][j]   o/p
0   0   l[0][0]    5
0   1   l[0][1]    6
0   2   l[0][2]    7

1   0   l[1][0]    3
1   1   l[1][1]    5
1   2   l[1][2]    8

2   0   l[2][0]    7
2   1   l[2][1]    5
2   2   l[2][2]    3

'''