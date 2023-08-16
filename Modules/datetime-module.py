'''
Datetime module 
If there is a need to perform manipulation on date and time use datetime module

'''

#datetime constant

import datetime

minyr=datetime.MINYEAR
print(minyr)
maxyr=datetime.MAXYEAR
print(maxyr)

#create datetime object

dtl=datetime.datetime(2017,3,23)
print(dtl)
dt2=datetime.datetime(2017,3,23,15,57,25)
print(dt2)
print ("Datatype:", type(dt2))

#system date and time now() and today()

a= datetime.datetime.now()
print(a)
b= datetime.datetime.today()
print(b)

print("Year:",a.year)
print(type(a.year))

print("Month:",a.month)
print(type(a.month))

print("day:",a.day)
print(type(a.day))

print("hour:",a.hour)
print(type(a.hour))

print("minute:",a.minute)
print(type(a.minute))

print("second:",a.second)
print(type(a.second))

