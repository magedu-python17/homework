from collections import Iterable
def fn1(n):
    return n % 2 == 1

def resemblefilter(fn,args):
    if isinstance(args, Iterable):
        lst = []
        for i in args:
            if fn(i):
                lst.append(i)
#                print(lst)
        return lst
    else:
        print("args is not iterable!")

print(tuple(resemblefilter(fn1,[2,3,3,4,5,6])))
#print(tuple(resemblefilter(lambda x:x%2==1 ,[2,3,3,4,5,6])))