# Palindrome without slicing

#n   i   t   i   n
#0   1   2   3   4
#i   i   ij  j   j
'''
i=0
j=4 1st s[0]==s[4] true

i=1
j=3 2nd s[1]==s[3] true

i=2
j=2 3rd s[2]==s[2] true
'''

s = input("enter a string: ")
print(s)

i=0
j=len(s)-1
while i<=j:
    if s[i]==s[j]:
        flag=1
    else:
        flag=0
        break
    i=i+1
    j=j-1

if flag==1:
    print("it is a palindrome")
else:
    print("it is not a paindrome")

