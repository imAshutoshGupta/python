#calculate age of the person based on dob
import datetime
dob=input("Enter Date of Birth in MM-DD-YYYY:")
db=dob.split('-')
print (db)
byear=int(db[2]) #year
print(byear)

#current year
cdt=datetime.datetime.now( )
cyear=cdt.year
print(cyear)
age=cyear-byear
print("Age is:",age)