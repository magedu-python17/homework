#!/usr/bin/env python


def sort1(iterable,reverse=False):
    if reverse == False:
        count = len(iterable)
        count2 = count // 2
        for i in range(count2):
            minindex = i
            maxindex = -i-1
            maxorigin = maxindex
            for j in range(i+1,count-i):
                if iterable[minindex] > iterable[j]:
                    minindex = j
                if iterable[maxindex] < iterable[-j-1]:
                    maxindex = -j-1
            if iterable[minindex] == iterable[maxindex]:
                break
            if i != minindex:
                iterable[i],iterable[minindex] = iterable[minindex],iterable[i]
                if i == maxindex or i == count + maxindex:
                    maxindex = minindex
            if maxorigin != maxindex and iterable[maxorigin] != iterable[maxindex]:
                iterable[maxorigin],iterable[maxindex] = iterable[maxindex],iterable[maxorigin]
        return iterable
    elif reverse == True:
        count = len(iterable)
        count2 = count // 2
        for i in range(count2):
            maxindex = i
            minindex = -i-1
            minorigin = minindex
            for j in range(i+1,count - i):
                if iterable[maxindex] < iterable[j]:
                    maxindex = j
                if iterable[minindex] > iterable[-j-1]:
                    minindex = -j-1
            if iterable[maxindex] == iterable[minindex]:
                break
            if i != maxindex:
                iterable[i],iterable[maxindex] = iterable[maxindex],iterable[i]
                if i == minindex or i == count + minindex:
                    minindex = maxindex
            if minorigin != minindex and iterable[minorigin] != iterable[minindex]:
                iterable[minorigin],iterable[minindex] = iterable[minindex],iterable[minorigin]
        return iterable


def sorted1(iterable,key=None,reverse=False):
    if key == None:
        if reverse == False:
            pass
    else:
        pass

list1 = [1,11,10,4,9,2,6,5,7]
print(sort1(list1,True))

