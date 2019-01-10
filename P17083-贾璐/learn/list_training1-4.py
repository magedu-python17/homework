#!/usr/bin/env python

import random

list1 = []
list2 = []
list3 = []
for i in range(10):
    e = random.randrange(0,21)
    list1.append(e)

for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
    else:
        if list3.count(i) == 0:
            list3.append(i)

print(list2)
print(list3)
print(list1)
