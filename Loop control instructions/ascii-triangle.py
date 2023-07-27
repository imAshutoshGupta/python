# a table with a constant ascii value
n = int(input("enter number of lines: "))
ascii_num=89
ch=chr(ascii_num)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(ch, end=" ")
    print()

# For a table with increment in ascii values

n = int(input("enter number of lines: "))

for i in range(1,n+1):
    an=65
    for j in range(1,i+1):
        ch = chr(an)
        print(ch, end=" ")
        an = an+1
    print()

# For a table with changing increment

n = int(input("enter number of lines: "))
an=65
for i in range(1,n+1):
    for j in range(1,i+1):
        ch = chr(an)
        print(ch, end=" ")
        an = an+1
    print()
