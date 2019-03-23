
from collections import Iterable
def fn1(x):
    return x*x

def fn2(x, y):
    return x + y

def fn3(n):
    return n%2==1
def mymap(fn,iter1):
    if not isinstance(iter1,Iterable):
        return 'Iterable is not Iterable'
    else:
        lst=[]
        for i in iter1:
            lst.append(fn(i))
    return lst

def myreduce(fn,iter1):
    if not isinstance(iter1,Iterable):
        return 'Iterable is not Iterable'
    else:
        lst=0
        for i in iter1:
            lst=fn(lst,i)
    return lst

def myfilter(fn,iter1):
    if not isinstance(iter1,Iterable):
        return 'Iterable is not Iterable'
    else:
        lst=[]
        for i in iter1:
            if fn(i):
                lst.append(i)
    return lst

print(mymap(fn1,(2,3,3,4,5,6)),'\n',mymap(fn1,123))
print(myreduce(fn2,(2,3,3,4,5,6)),'\n',myreduce(fn2,123))
print(myfilter(fn3,(2,3,3,4,5,6)),'\n',myfilter(fn3,123))

# 这里如果不支持的话，最好raise 错误，而不是用return

