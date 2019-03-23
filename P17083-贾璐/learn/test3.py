#!/usr/bin/env python
iterable = [1,2,3,4,5,6,7,8,9]
count = len(iterable)
count2 = count // 2
for i in range(count2):
    maxindex = i
    minindex = -i-1
    minorigin = minindex
    for j in range(i+1,count-i):
        if iterable[maxindex] < iterable[j]:
            maxindex = j
        if iterable[minindex] > iterable[-j-1]:
            minindex = -j-1
    if iterable[maxindex] == iterable[minindex]:
        break
    if i != maxindex:
        iterable[i],iterable[maxindex] = iterable[maxindex],iterable[i]
        print(iterable)
        if i == minindex or i == count + minindex:
            minindex == maxindex
    if minorigin != minindex and iterable[minorigin] != iterable[minindex]:
        iterable[minorigin],iterable[minindex] = iterable[minindex],iterable[minorigin]
        print(iterable)

print(iterable)
