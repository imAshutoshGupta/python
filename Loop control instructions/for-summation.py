#summation from 1 to n with for

n=int(input("enter last term: "))
'''
i=1  #start
s=0
while i<n:   #stop
    s=s+i
    i+=1     #step
print(s)
'''

s=0
for i in range(1,n+1,1):
    s=s+i
print(s)