#tuple methods 
#count: it is used to count occurance of a element in a tuple

t = (12,20,45,65,'abc','xyz','abc',45,65,20)
print(t)

n1 = t.count(20)
print("occurance of 20: ",n1)

n2 = t.count(45)
print("occurance of 45: ",n2)

n3 = t.count('abc')
print("occurance of abc: ",n3)

# index(): this method returns the index of first occurance of the value incase of repetition

i1 = t.index(65)
print(i1)
i2 = t.index(45)
print(i2)

