#rules for mobile number validation
'''
rule 1 - must be 10 digit
rule 2 - must be a number and not alphabets or symbols
'''

mn = input("enter mobile number: ")

l = len(mn)
print("length of input is", l) 
if l==10:
    if mn.isdigit():
        print("hence it's a valid mobile number")
    else:
        print("hence it's an invalid mobile number")
else:
    print("hence it's an invalid mobile number")