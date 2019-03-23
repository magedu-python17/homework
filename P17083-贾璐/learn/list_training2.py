#!/usr/bin/env python

list1 = list(range(1,1001))
list2 = []
for i in range(len(list1)):
    if list1[i] == 1 or list1[i] % 2 == 0 and list1[i] != 2:
        list2.append(list1[i])
    else:
        for n in range(2,int(list1[i] ** 0.5) + 1):
            if list1[i] % n == 0:
                list2.append(list1[i])

list3 = list(set(list1).difference(set(list2)))
print(len(list3))
