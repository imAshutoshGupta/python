# max, min, pow, id
l = [10,3,4,5,7,5,44,65,43,67,2]

mx = max(l)
print("maximum value: ", mx)

mn = min(l)
print("minimum value: ", mn)

lrev = list(reversed(l))      #reversed object to list object
print(lrev)

trev=tuple(reversed(l))
print(trev)

srev= set(reversed(l))
print(srev)

#power
n=3
p=-2

res=pow(n,p)
print(res)

#memory addess
x=10
print(x)
print(type(x))

idx = id(x)
print("memory address of",x,":",idx)


y=10
print(y)
print(type(y))

idy = id(y)
print("memory address of",y,":",idy)
