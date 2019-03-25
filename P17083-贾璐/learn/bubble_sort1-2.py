#!/usr/bin/env python

lst = [int(x) for x in input("Enter numbers: ").split(" ")]
count = len(lst)
count2 = count // 2
for i in range(count2):
    minindex = i
    maxindex = -i-1
    maxorigin = maxindex
    for j in range(i+1,count - i):
        if lst[minindex] > lst[j]:
            minindex = j
        if lst[maxindex] < lst[-j-1]:
            maxindex = -j-1
    if lst[maxindex] == lst[minindex]:
        break
    if i != maxindex:
        lst[i],lst[minindex] = lst[minindex],lst[i]
        if i == maxindex or i == count + maxindex:
            maxindex = minindex
    if maxorigin != maxindex and lst[maxorigin] != lst[maxindex]:
        lst[maxorigin],lst[maxindex] = lst[maxindex],lst[maxorigin]

print(lst)
        
