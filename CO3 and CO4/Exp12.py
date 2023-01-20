import datetime
t=datetime.datetime.now()
tt=t+datetime.timedelta(0,5)
print("Current Time:",t.time())
print("5 sec after current time",tt.time())
