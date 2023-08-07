# s = "we:are:learning split:and join methods"
#print(s)

# l = s.split()     #default sep is space
#print(l)
# l = s.split(':')
# print(l)

l = ['we','are','learning','join method']
t = ('we','are','learning','join method')
print(t)

#'binder'.join(collection)

s='-'.join(t)
print(s)
print(type(s))

