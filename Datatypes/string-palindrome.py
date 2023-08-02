#WAP to check if the string is palindrome or not

org = input("enter a string: ")
rev = org[::-1]
print("original string: ",org)
print("reversed string",rev)

if org==rev:
    print("string is a palindrome")
else:
    print("not a palindrome")

# Lower the string and then check

org = input("enter a string:")
temp = org.lower()
print("lowered string",temp)
print("reversed string",rev)

if temp==rev:
    print("string is a palindrome")
else:
    print("not a palindrome")