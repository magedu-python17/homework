#!/usr/bin/env python
list1 = []
count = int(input(">>> "))

for i in range(count):
    row = [1] * (i+1)
    list1.append(row)
    for j in range(1,i // 2 + 1):
        val = list1[i - 1][j - 1] + list1[i - 1][j]
        row[j] = val
        if i != 2 * j:
            row[-j-1] = val
    print(row)
