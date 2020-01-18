from datetime import date
import datetime
import calendar

weekDays= {0:'Monday',1:'Tuesday',2:'Wednesday',3: 'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

now = datetime.datetime.now()
current_year = now.year


name = input("Enter your name:")
#print (name)

###########get dob
dob = input('Enter your DOB in YYYY-MM-DD format:\n')
yy, mm, dd = map(int, dob.split('-'))
#print(dob) 
#print(yy,mm,dd)

dob1 = date(yy, mm, dd)
#print(dob1)

###########get age

age = now.year - dob1.year - ((now.month, now.day) < (dob1.month, dob1.day))

ageInt = int(age)




birth_year = (current_year - ageInt)
op = birth_year + 100

opDate = date(op,mm,dd)
#print(opDate)
opDay = opDate.weekday()
#print(opDay)


hunDay = weekDays[opDay]

print("\n")

print("Hi" ,name, ",Your present age is" ,age,"\n" "You'll complete your CENTURY in year " ,op)

print('\n')

print("Your 100th Birthday is falling on ",hunDay,"!!")