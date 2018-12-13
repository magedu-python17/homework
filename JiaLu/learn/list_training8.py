#!/usr/bin/env python

count = 3
list1 = []
while count > 0:
    num = int(input(">>> "))
    list1.append(num)
    count -= 1
list1.sort()
print(list1)
