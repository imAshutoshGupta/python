#filter negative positive numbers in a list
l = [12,-34,5,-6,7,-85,65,9,-3,0]
lpositive = []
lnegative = []
lzero = []
for x in l:

    if x>0:
        lpositive.append(x)
    elif x==0:
        lzero.append(x)
    else:
        lnegative.append(x)
print("positive number: ", lpositive)
print("negative number: ", lnegative)
print("zero: ", lzero)