"""
from datetime import datetime, timedelta

current_date = datetime.today()

new_date = current_date - timedelta(days=5)

print( new_date.strftime("%Y-%m-%d"))

"""

"""
import datetime

x = datetime.datetime.now()

print(x.day - 1)
print(x.day)
print(x.day + 1)
"""

"""
import datetime

x = datetime.datetime.now().replace(microsecond=0)

print(x)

"""
import datetime

d1 = datetime.datetime(2024, 2, 20, 12, 0, 0)
d2 = datetime.datetime(2024, 2, 21, 14, 30, 0)

dif = abs((d2 - d1).total_seconds())
print("Difference in seconds: ", int(dif))


