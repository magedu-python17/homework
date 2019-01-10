#!/usr/bin/env python

import random

list1 = []
list2 = []
list3 = []
for i in range(10):
    list1.append(random.randrange(0,21))


for i in list1:
    if i not in list2:
        list2.append(i)
    elif i not in list3:
        list3.append(i)

set2 = set(list2)
set3 = set(list3)

print(set3)
print(set2 ^ set3)
print(list1)
