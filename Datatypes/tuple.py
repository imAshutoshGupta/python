'''
tuple
1) it is a collection of dissimilar datatype.
2) it is represented by () or paranthesis.

'''

t=(10,20,"itvedant",56.6)
print(t)
print("Datatype: ",type(t))
n=len(t)
print("total number of elements in tuple: ",n)

#indexing: to access element in collection-tuple
'''
(10,20,"itvedant",56.6)
 0   1     2        3  
 -4  -3    -2      -1

 tuple_object[index]
'''
#accessing
print(t[2])
print(t[-3])

#slicing: to access partial part of tuple
# tuple_object[start,stop,step]
t1=t[1:3]
print(t1)

#reverse
trev = t[::-1]
print(trev)

# add,update and remove tuple element
# tuple are immutable
'''
t[2] = "itvedant-thane"
print(t)
'''

# for loop over tuple
# index
print("for loop with index")
for i in range(0,len(t)):
    print(t[i])

print("for loop without index:")
for x in t:
    print(x)

#del keyword
del t
print(t)
