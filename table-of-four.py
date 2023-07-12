i=1
while i<=10:
    t=4*i
    print("4 *",i,"=",t)
    i=i+1
    
    #dry run
    #i<=10  t=4      print(t)    i=i+1
    #1<=10  t=4*1    print(4)    i=1+1
    #2<=10  t=4*2    print(8)    i=2+1
    #3<=10  t=4*3    print(12)   i=3+1
    #4<=10  t=4*4    print(16))  i=4+1
    #5<=10  t=4*5    print(20)   i=5+1
    #6<=10  t=4*6    print(24)   i=6+1
    #7<=10  t=4*7    print(28)   i=7+1
    #8<=10  t=4*8    print(32)   i=8+1
    #9<=10  t=4*9    print(36))  i=9+1
    #10<=10 t=4*10   print(40)   i=10+1
    
    
    
    # FOR "n"
    
n = int(input("enter your number: "))
j=1
while j<=10:
    r=n*j
    print("your number *",j,"=",r)
    j=j+1
    
    
    # number shouldnt be Zero
    
n = int(input("enter your number: "))

if n>0:
 k=1
while k<=10:
        s=n*k
        print("your number *",k,"=",s)
        k=k+1
else:
    print("invalid input")