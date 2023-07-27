# CONTINUE IS ALWAYS USED WITH IF KEYWORD
i=1
while i<=10:
    if i==4:
        i=i+1
        continue
    print(i)
    i=i+1


# Infinite loop
i=1
while i<=10:
    if i==4:
        print("hahaha")
        continue
    print(i)
    i=i+1