import datetime
import time
# print(time.time())
print(time.asctime(time.localtime(time.time())))
datetime_obj=datetime.datetime.now()
print(datetime_obj)
print("year :",datetime_obj.year)
print("month: ",datetime_obj.month)
print("day: ",datetime_obj.day)
print("hour :",datetime_obj.hour)
print("minute :",datetime_obj.minute)

