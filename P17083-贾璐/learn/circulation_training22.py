#!/usr/bin/env python
import datetime
num = int(input("Enter a number: "))
count = 1
start = datetime.datetime.now()
for i in range(3,num,2):
    if i > 10 and i % 10 == 5:
#    if i > 11 and i % 6 !=5 and i % 6 != 1:
        continue
    for j in range(3,int(i ** 0.5 + 1),2):
        if i % j == 0:
            break
    else:
        count += 1
#        print(i) 
end = datetime.datetime.now()

times = (end - start).total_seconds()
print(count)
print(times)

