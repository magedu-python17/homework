#!/usr/bin/env python

lst = [5,6,2,1,9,3,8,4,7]

count = len(lst)
for i in range(count):
    maxindex = i
    for j in range(i+1,count):
        if lst[j] > lst[maxindex]:
            maxindex = j
    if i != maxindex:
        lst[i],lst[maxindex] = lst[maxindex],lst[i]

print(lst)
        
