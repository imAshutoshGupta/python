# convert ascii value into character

n = int(input("enter value: "))
ch = chr(n)
print("corresponding ascii character is: ", ch)


for i in range(0,256):
    ch=chr(i)
    print(i, '-', ch)
    