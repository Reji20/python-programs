from datetime import datetime,timedelta
now=datetime.now()
time=now.time()
print('Current Time :',time)
today=datetime.today()
d=today-timedelta(5)
print('5 days before current date :',d)
print('Current Date :',today)
print('Yesterday :',today-timedelta(1))
print('Tommorrow :',today+timedelta(1))
print('Next 5 days from today :')
for i in range(1,6):
    t=today+timedelta(i)
    print(t)
s=now+timedelta(0,5)
print('Time after 5 seconds :',s.time())
