# Calculate your Age in Seconds

from datetime import datetime

year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
date = int(input("Enter birth date: "))

res = (datetime.now() - datetime(year, month, date)).total_seconds()
print(f"You are {res} seconds old.")