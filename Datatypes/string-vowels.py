# WAP to count the number of vowels and consonants

s = input("enter string: ")
v=0
c=0
for x in s:
    if x in ('a','e','i','o','u','A','E','I','O','U'):
        v += 1
    else:
        c=c+1

print("number of vowels: ", v)
print("number of consonants: ",c)

# convert to lower and now run the same program

s = input("enter string: ")
v=0
c=0
t = s.lower()
print(t)
for x in s:
    if x in ('a','e','i','o','u'):
        v += 1
    else:
        c=c+1

print("number of vowels: ", v)
print("number of consonants: ",c)











