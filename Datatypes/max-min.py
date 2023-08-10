# max element

l = [20,30,-1,3,49,29]
max = l[0]

for x in l:
    if x>max:
        max = x
print("maximum element: ", max)

# min element

l = [20,30,-1,3,49,29]
min = l[0]

for x in l:
    if x<min:
        min = x
print("maximum element: ", min)

# both in one

x=[20,30,-1,3,49,29]
mx=max(x)
mi=min(x)
print ("Maximum Element in the list:",mx)
print ("Minimum element in the list: ", mi)