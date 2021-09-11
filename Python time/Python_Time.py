import datetime
import calendar
import time

localtime = time.localtime(time.time())
print("local time:", localtime)
# local tome: time.struct_time(tm_year=2021, tm_mon=9, tm_mday=11, tm_hour=14, tm_min=47, tm_sec=46, tm_wday=5, tm_yday=254, tm_isdst=0)

localtime = time.asctime(time.localtime(time.time()))
print("local time:", localtime)
# local time: Sat Sep 11 14:48:37 2021

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 2021-09-11 14:49:34

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# Sat Sep 11 14:50:01 2021

test_time = "Sat Mar 28 22:24:24 2021"
print(time.mktime(time.strptime(test_time, "%a %b %d %H:%M:%S %Y")))
# 1616941464.0

### import calendar
# 月曆
Pycalendar = calendar.month(2021, 6)
print("Calendar 2021 june")
print(Pycalendar)
#     June 2021
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30


### import datetime
i = datetime.datetime.now()
print("Current datetme %s" % i)
print("ISO datetme %s" % i.isoformat())
print("Current year %s" % i.year)
print("Current month %s" % i.month)
print("Current day %s" % i.day)
print("dd/mm/yyyy Format  %s/%s/%s" % (i.day, i.month, i.year))
print("Current hour %s" % i.hour)
print("Current minute %s" % i.minute)
print("Current second %s" % i.second)
