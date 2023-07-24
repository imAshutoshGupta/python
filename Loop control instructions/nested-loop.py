# Nested Loop

# DRY RUN
#i   i->3   print(i)    j   j       print(j)
#1   i->3       1_      1   j->4     1_2_3
#                       2
#                       3
#
#
#2  2->3       2_       1
#                       2
#                       3

for i in range(1,3,1):      #[1,2]
    print(i, end=" ")
    for j in range(1,4,1):      #[1,2,3]
        print(j, end=" ")
    print()











