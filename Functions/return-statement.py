#return statement helps to return a value from function body to function call

#return statement
num=int (input ("Enter a number:"))
def facto (n):
    fact=1
    for i in range (1, n+1):
        fact=fact*i
    return fact
t=facto (num)
print ("Factorial of", num, ": ", t)
print (num, " !=",t)