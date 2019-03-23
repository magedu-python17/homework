from collections import Iterable
def fn(x):
    return x*x
def resemblemap(fn,args):
    if isinstance(args, Iterable):
        lst = []
        for i in args:
            lst.append(fn(i))
        for j in lst:
            yield j
    else:
        print("args is not iterable!")
#print(tuple(resemblemap(str,[1,2])))
#print(list(resemblemap(lambda x:2*x+1,range(5))))
#print(list(resemblemap(fn,range(5))))


def fn1(n):
    return n % 2 == 1

def resemblefilter(fn,args):
    if isinstance(args, Iterable):
        lst = []
        for i in args:
            if fn(i):
                lst.append(i)
        for j in lst:
           yield j
    else:
        print("args is not iterable!")

#print(tuple(resemblefilter(fn1,[2,3,3,4,5,6])))
#print(tuple(resemblefilter(lambda x:x%2==0 ,[2,3,3,4,5,6])))

def fn2(x,y):
    return x + y

def resemblereduce(fn,args):
    if isinstance(args, Iterable):
        tmp = fn(args[0],args[1])
        lst = args[2:]
        for i in lst:
            tmp1 = fn2(tmp,i)
            tmp  = tmp1
        return tmp
    else:
        print("args is not iterable!")

#print(resemblereduce(fn2,[1,2,3,4,5]))
#print(resemblereduce(lambda x, y: x+y,[1,2,3,4,5]))

# 高阶函数这边少个错误的提示，参考下raise的用法，再来完善下