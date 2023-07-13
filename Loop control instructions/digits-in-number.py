# WAP to count number of digits in an entered number.

# count=0
#n=5698     n=n//10=5698//10=569        count=count+1=0+1=1
#n=569      n=n//10=569//10=56          count=count+1=1+1=2
#n=56       n=n//10=56//10=5            count=count+1=2+1=3
#n=5        n=n//10=5//10=0             count=count+1=3+1=4
#n=0        n=0

n = int(input("enter the number you want to count: "))
count = 0

while n>0:
    count=count+1
    n=n//10

print("number of digits:",count)