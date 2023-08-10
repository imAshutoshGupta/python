# factorial using recursion

num=int (input("Enter number:"))

def factorial (n):
    if n==1:
            return 1
    s=n*factorial (n-1);
    return s
r=factorial (num)
print ("factorial is:",r)