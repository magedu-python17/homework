#!/usr/bin/env python

#lst = [5,6,2,1,9,3,8,4,7]

lst = [1,1,1,1,1,1,1,1,1,2]
count = len(lst)
count2 = count // 2
for i in range(count2):
    maxindex = i
    minindex = -i-1
    minorigin = minindex
    for j in range(i+1,count - i):
        if lst[maxindex] < lst[j]:
            maxindex = j
        if lst[minindex] > lst[-j-1]:
            minindex = -j-1
    if lst[maxindex] == lst[minindex]:
        break
    if i != maxindex:
        lst[i],lst[maxindex] = lst[maxindex],lst[i]
        if i == minindex or i == count + minindex:
            minindex = maxindex
    if minorigin != minindex and lst[minorigin] != lst[minindex]:
        lst[minorigin],lst[minindex] = lst[minindex],lst[minorigin]

    print(lst)
print(lst)
        
