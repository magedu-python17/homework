#!/usr/bin/env python
n = int(input(">>> "))

list1 = []

for i in range(2,n+1):
    check = 0
    up = i ** 0.5
    if i == 2:
        list1.append(i)
    else:
        for a in list1:
            if i % a == 0:
                check = 1
                break
            if a >= up:
                break
        if check != 1:
            list1.append(i)
print(len(list1))
