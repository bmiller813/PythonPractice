from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000) 
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("Days: ", duration.days)
print("Seconds: ", duration.seconds)
print("Total Seconds: ", duration.total_seconds())