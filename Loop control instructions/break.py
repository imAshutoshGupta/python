#break keyword
# BREAK IS ALWAYS USED WITH IF KEYWORD

for i in range(1,11,1):
    if i==5:
        break
    print(i)

'''
i   []     i==5        print(i)
1   T      1==5        1
2   T      2==5        2
3   T      3==5        3
4   T      4==5        4
5   T      5==5        break
'''

for i in range(1,11,1):
    print(i)
    if i==5:
        break


    # ELSE

for i in range(1,11,1):
    if i==5:
        break
    print(i)
else:
    ("else part")     #when the condition is false the loop enters else part

# in the above program due to break keyword loop gets terminated but the condition remains true thus it will not execute else part

