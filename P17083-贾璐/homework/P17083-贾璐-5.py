#!/usr/bin/env python

from collections import Iterable

def map(func_name,*iters):
    func = func_name
    iters = list(iters)
    lenth = len(iters)
    nums = []
    rets = []
    if type(iters[0]) == list:
        for i in iters:
            if isinstance(i,Iterable) == False:
                print("Please input iterables!")
                return None
        for i in range(lenth):
            nums.append(len(iters[i]))
        min_num = min(nums)
        for i in range(min_num):
            v = []
            for j in range(lenth):
                v.append(iters[j][i])
            ret = func(*v)
            rets.append(ret)
        return rets
    else:
        for i in iters:
            ret = func(i)
            rets.append(ret)
        return rets

def reduce(func_name,*iters):
    func = func_name
    iters = list(iters)
    lenth = len(iters)
    if type(iters[0]) == list:
        ret = 0
        if func(ret,1) == 0:
            ret = 1
        nums = iters[0]
        if lenth > 1:
            for i in range(1,lenth):
                if isinstance(iters[i],Iterable) == False:
                    nums.append(iters[i])
                else:
                    nums += iters[i]
        for i in nums:
            ret = func(ret,i)
        return ret
    else:
        ret = 0
        if func(ret,1) == 0:
            ret = 1
        for i in iters:
            ret = func(ret,i)
        return ret 

def filter(func_name,*iters):
    func = func_name
    iters = list(iters)
    lenth = len(iters)
    rets = []
    if type(iters[0]) == list:
        nums = iters[0]
        if lenth > 1:
            for i in range(1,lenth):
                if isinstance(iters[i],Iterable) == False:
                    nums.append(iters[i])
                else:
                    nums += iters[i]
        for i in nums:
            ret = func(i)
            if ret == True:
                rets.append(i)
        return rets
    else:
        for i in iters:
            ret = func(i)
            if ret == True:
                rets.append(i)
        return rets


def fnc(x):
    #return x+y
    return x % 2 == 0

#print(list(map(lambda x,y:x+y,[1,2,3],[4,5])))
#print(list(map(lambda x: x * x , 1,2,3,4)))

#print(reduce(fnc,[1,2,3],[1,2]))
print(filter(fnc,[1,2,3,4]))
