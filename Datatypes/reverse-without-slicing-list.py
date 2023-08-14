#reverse a list without slicing
#hint - we will use insert()

l = [10,20,30,40]

lrev = []

lrev.insert(0,l[0])    #0 is the index and l[0] is the element to be inserted
print(lrev)
lrev.insert(0,l[1])
print(lrev)
lrev.insert(0,l[2])
print(lrev)
lrev.insert(0,l[3])
print(lrev)

# using for loop
c = [10,20,30,40]
crev = []
for x in c:
    crev.insert(0,x)
print(crev)