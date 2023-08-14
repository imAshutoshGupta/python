# captcha generation
import string as s
import random as r

a = s.ascii_letters+s.digits
captcha = ""

for i in range(1,6):
    ind = r.randrange(0,62)
    print(ind)

    ch = a[ind]
    print(ch)

    captcha = captcha + ch
    print(captcha)
    print()

print("captcha is:", captcha)



