#!/usr/bin/env python
import datetime
num = int(input("Enter a number: "))

strs = ""
count = 0

start = datetime.datetime.now()
for i in range(2,num):
    for c in range(2,int(i ** 0.5)+1):
        if i % c == 0:
             break
    else:
        count += 1
        strs += str(i) + " "
#print(strs)
end = datetime.datetime.now()

times = (end - start).total_seconds()
print(times)
print(count)
