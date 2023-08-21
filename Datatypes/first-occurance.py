#find the position of the first occurance of the element given by user in the list
s = int(input("enter number to search in list: "))
l = [10,2,3,4,5,6,4,6,7,5,6,56,78,5,44,65,7,7,545,4,7]
print(l)

for i in range(0,len(l),1):         # i = 0,1,2,3,4,5,6,7,8
    if s==l[i]:
        print("element found at",i+1,"position")
        break
else:
    print("not found")
