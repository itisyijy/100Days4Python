# Day32 for 100Days4Python
# Day32 : Datetime

import datetime as dt

# Current Time
now = dt.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day
now_weekday = now.weekday() # 0 MON / 1 TUE / 2 WED / 3 THU / 4 FRI / 5 SAT / 6 SUN
print(now_year, now_month, now_day, now_weekday)

my_birthday = dt.datetime(year=1948, month=8, day=15)
print(my_birthday)
