#!/usr/bin/env python

list1 = []
for i in range(101):
    if i == 0:
        list1.append(1)
    else:
        if i == 1:
            list1.append(1)
        else:
            sum1 = list1[i-2] + list1[i-1]
            list1.append(sum1)

print(list1[100])
