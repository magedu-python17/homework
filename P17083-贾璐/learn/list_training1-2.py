#!/usr/bin/env python

from copy import deepcopy

list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = deepcopy(list1)

for i in range(len(list1)):
    for j in range(i):
        list2[j][i] = list1[i][j]

print(list2)
