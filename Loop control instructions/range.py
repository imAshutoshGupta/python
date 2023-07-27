'''
syntax:
range(start,stop,step)

'''

#num=range(1,10,1)
#print(num)

num=list(range(0,10,1))
num=list(range(1,10,2))
num=list(range(1,10,3))

#step negative
num=list(range(1,10,-2))
num=list(range(10,1,-2))

# Default value of step in range is one
num=list(range(0,10))
print(num)

# Default value of start in range is zero
num=list(range(10))
print(num)
