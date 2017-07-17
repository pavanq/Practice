y=input("Input a year:")
m=input("Input a month[1-12]:")
d=input("Input a day[1-31]:")
from datetime import date,timedelta
x=date(y,m,d)
print (x+timedelta(1))
