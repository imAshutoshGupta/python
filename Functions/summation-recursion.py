# summation of 1 to n by using recursion

num=int (input("Enter number:"))

def summation (n):
    if n==1:
            return 1
    s=n+summation (n-1);
    return s
r=summation (num)
print ("Summation is:",r)