#variable length argument
def addition (*x): #x=(10,) | x=(10, 20) |x=(10,20,30)
    #print (x)
    #print (type (x))
    s=0
    for i in x: # (10,)| (10,20) | (10,20,30)
        #print (i)
        s=s+i
    print ("Summation is:",s)
addition (10)
addition (10,20)
addition (10,20,30)