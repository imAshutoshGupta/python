#search an element enterted by user in a given list (linear search)
l = [1,10,-12,32,454,64,2,46,76,-46,-54]
n = int(input("enter element to be searched: "))

for x in l:
    if x==n:
        print("element found")
        break

else:
    print("element not found")
