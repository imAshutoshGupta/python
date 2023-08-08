#filter odd numbers from a list

l = [12,3,45,67,4,3,56,68,8]
print("ODD NUMBERS")
for x in l:
    r=x%2
    if r!=0:
        print(x)


#filter even numbers from a list

l = [12,3,45,67,4,3,56,68,8]
print("EVEN NUMBERS")
for x in l:
    r=x%2
    if r==0:
        print(x)


# add elements to an empty list

l = [12,3,45,67,4,3,56,68,8]
lodd = []               # way to create an empty list
leven = list()          #another way to create an empty list

for x in l:
    r=x%2
    if r!=0:
        lodd.append(x)
    else:
        leven.append(x) 

print("original list: ",l)       
print("odd list: ",lodd)       
print("even list: ",leven)       








