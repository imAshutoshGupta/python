# Fibonacci series
# 0,1,1,2,3,5,8...

#i=0
#j=1
#print(i)
#print(j)

# i=0 j=1       t=i+j             print(t)        i=j j=t
# i=1 j=1       t=i+j=1+1=2       print(t)        i=j j=t
# i=1 j=2       t=i+j=1+2=3       print(t)        i=j j=t
# i=2 j=3       t=i+j=2+3=5       print(t)        i=j j=t

n= int(input("enter number of terms: "))
i=0
j=1
print(i, end=" ")
print(j, end=" ")
k=1

while k<=n-2:
    t=i+j
    print(t, end=" ")
    i=j
    j=t

    k+=1  #k=k+1

