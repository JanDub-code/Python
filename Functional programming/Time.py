import datetime

from datetime import datetime as dt
from datetime import date as d
from datetime import time as t
from datetime import timedelta as td

d = datetime.date(2034,8,28)
new_d = d + datetime.timedelta(days=14)
print(new_d)

new_d = d + datetime.timedelta(days=14, seconds=24*3600)
print(new_d)

d1 = datetime.date(1970, 1, 1)
d2 = datetime.date(1970, 1, 15)
td = d2-d1
print(td)
print(td.seconds)
print(td.days)

dt = datetime.datetime(2034, 12, 31, 10, 12, 34)
new_dt = dt - datetime.timedelta(12,34)
print(new_dt)

d = datetime.date(2034, 8, 28)
new_d = d - datetime.timedelta(seconds=24*3600)
print(new_d)

t = datetime.date.today()
print(t)

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
#formating like we want it
my_d = datetime.date(1970, 1, 1)
my_dt = datetime.datetime(1970, 1, 1, 17, 34, 54, 654)
print(my_d.strftime('%d.%m.%Y %H:%M:%S'))
print(my_dt.strftime('%d.%m.%Y %H:%M:%S'))

formatted = '01/01/1970 17:34:54'
print(dt.strptime(formatted,'%d/%m/%Y %H:%M:%S'))
formatted2 = '01/01/1970'
print(dt.strptime(formatted2,'%d/%m/%Y'))

dt = datetime.datetime(2016, 8, 21, 11, 32)
print(dt.weekday())

print(datetime.date.today().weekday())

#for measuring what is fastest solution
import time
i=0
size = 36000
start = time.time()
while i<size:
    i+=1
end = time.time()
print('Iterated {} times in {} seconds'.format(size, end-start))