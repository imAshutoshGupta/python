#intersection of sets
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print("set 1:", s1)
print("set 2: ", s2)

#intersection()

s_inter =  s1.intersection(s2)
print("intersection: ",s_inter)

#union

s_union = s1.union(s2)
print("union: ", s_union)

#strings

s3={"abc","xyz","pqr"}
s4={"pqr","rst"}

c= s3.intersection(s4)
d=s3.union(s4)
print(c)
print(d)