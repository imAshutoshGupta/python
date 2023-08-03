# set is a collection of unordered elements 
# reason - SETS DONT HAVE INDEX
# they contains only unique values. no duplicate values

s = {12,20,'itvedant',35.6,20,12,69}
print(s)
print("datatype:",type(s))
l = len(s)
print("length:", l)

#print(s[1]) => error
#indexing => no
#slicing => error

# adding element in set
# add(): this method is used to add element into set
s.add(199)
print(s)

#update(): this is used to add any collection in set

s1 = {150,260}
print("s1:",s1)
s.update(s1)
print(s)

l=[1000,2000]
print(l)
s.update(l)
print(s)

#pop(): always delete last element
#randomly deletes here incase of sets as we dont know which element is last (unordered)

s.pop()
print(s)

#remove(): to delete a specific element from set
#set_obj.remove(value)

s.remove(20)
s.remove(35.6)
print(s)

#discard()

s.discard(1)
s.discard(35.6)
print(s)

#difference between remove and discard
#remove is strict and removes the element and raises an error if the value isnt in the set
#discard is not strict and does not give any key error even if the element is not present in the set

#for loop over set
for x in s:
    print(x)

del(s)
print(s)
