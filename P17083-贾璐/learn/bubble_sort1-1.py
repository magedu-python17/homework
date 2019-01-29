#!/usr/bin/env python

lst = [int(x) for x in input("Enter numbers: ").split(" ")]
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
        
