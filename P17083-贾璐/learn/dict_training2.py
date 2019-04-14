#!/usr/bin/env python
import random

d = {}

count = 100

while count > 0:
    num = random.randint(-1000,1001)
    if num not in d.keys():
        d[num] = 1
    else:
        d[num] += 1
    count -= 1

lst = list(d.keys())
lst.sort(reverse=True)
for key in lst:
    print("{}:{}".format(key,d[key]))

