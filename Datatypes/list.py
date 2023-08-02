'''
List 
1) it is a collection of dissimilar datatypes
2) in list elements are enclosed in sq brackets[]
'''

l = [10,20,'itvedant',35.6]
print(l)
print(type(l))

#len(): return the number of elements in the list

n=len(l)
print("total number of elements in the list:", n)

#Indexing: accessing elements
#list_object[index]
'''
[10,20,'itvedant',35.6]
 0   1      2       3
 -4  -3     -2      -1
'''
print(l[2])
print(l[-3])

#Slicing: slice of list or partial part of list
#list_object[start:stop:step]

l1=l[1:3:]
print(l1)

l2=l[-1:-4:-1]
print(l2)

lrev=l[::-1]
print(lrev)

'''
element in list can be added in two ways
1) append(): this method adds elements at the end of list
2) insert(): this method adds elements at the specific index
'''

l.append(25)
print(l)

l2=[100,200]
l.append(l2)
print(l)

l.insert(2,30) #insert(index,value)
print(l)

#addition of list using + operator
l1 = [45,67,90]
l3 = l+l2
print(l2)
print(l3)

#updating list elements
#list_object[index] = new value
l[2] = "itvedant-thane"
print(l)

#remove
print("remove homework")
l.remove(20)
print(l)

#pop()
l.pop()
print(l)

l.pop(2)
print(l)

#remove removes element with value and pop will always remove the element with value




#for over list with index
print("for with index")
for i in range(0,len(l)):
    print(l[i])

print("for without index")
for x in l:
    print(x)

# replace
w = [1,2,3,4,5,6,7,8,9]
w[4] = 4
print(w)

#del l
#print(l)
hello = "hi i am a human"
p = hello.replace("human","animal")
print(p)

# check palindrome string
# using slicing to reverse a string
# and without slicing
# find summation of elements in a list
# filter only odd numbers from the given list
# program to reverse a list without slicing
#sort a given list (bubble sort)
# search an element entered by user in a given list (linear search)
# find the position of first occurance of an element entered by user in the given list
# find the position of all occurances of an element entered by user in a given list


