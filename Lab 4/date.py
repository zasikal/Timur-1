from datetime import datetime
from datetime import timedelta
#1


x=datetime.now()
print("5 days ago:", x - timedelta(days=5))
#2

print("yesterday:", x - timedelta(days=1))
print("today", x)
print("tomorrow:", x + timedelta(days=1))

#3
print("without microseconds: ", x.replace(microsecond=0))
#4
date1 = datetime(2025, 2, 17, 23, 22, 43)
date2 = datetime(2025, 2, 17, 23, 24, 23)
print("difference in seconds: ", (date2-date1).total_seconds())