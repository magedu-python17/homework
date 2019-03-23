#!/usr/bin/env python

list1 = []
list2 = []
for i in range(100):
    if i == 0:
        list1.append(1)
        list2.append(1)
    else:
        if i == 1:
            list1.append(1)
            list2.append(1)
        else:
                sum1 = list1[i-2] + list1[i-1]
                if sum1 < 100:
                    list2.append(sum1)
                list1.append(sum1)

print(list2)
