# SYNTAX -  class datetime.date(year, month, day)

# 1) DEMONSTARTING DATE CLASS
from datetime import date

my_date = date(2003,5,19)
print(f"D.O.B -> {my_date}")


# 2) DEMONSTRATING CURRENT DATE
# i)
from datetime import date

my_date = date.today()
print(f"Displays Current Date: {my_date}")


# ii) 
from datetime import date

today = date.today()
print(f"Year: {today.year}\nMonth: {today.month}\nDate: {today.day}")


# 3) DEMONSTRATE DATE AND TIME


from datetime import datetime

now = datetime.now()
print(f"Current DATE & TIME: {now}")
