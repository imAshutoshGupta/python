n = int(input("enter your number: "))

# if n>=100 and n<=999:
if 100<= n <=999:
    a=n%10
    b=n//10
    c=b%10
    d=b//10
    t = a**3 + c**3 + d**3
    if t==n:
        print("armstrong number")
    else:
        print("not armstrong")
else:
    print("out of range")