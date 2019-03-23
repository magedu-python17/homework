#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-03-04 23:08
#
# Filename: HomeworkForWeek05.py
#
# Description: V1.0
#
#========================================================
def fn(x):
    return x * x

def mapself(fn,iterable):
    if not isinstance(iterable,(dict,list,tuple,set)):
        print("ERROR")
    else:
        for i in iterable:
            yield fn(i)

print(mapself(fn,[1,2,3,4,5]))
lst = list(mapself(fn,[1,2,3,4,5]))
print(lst)
################
def fn(x):
    return x % 2 == 1

def filterself(fn,iterable):
    lst = []
    if not isinstance(iterable,(dict,list,tuple,set)):
        print("ERROR")
    else:
        for i in iterable:
            if fn(i) == True:
                lst.append(i)
    return lst

print(filterself(fn,[1,2,3,4,5,6,7,8,9]))
#########
def fn(x,y):
    return x + y
def reduceself(fn,iterable):
    if not isinstance(iterable,(dict,list,tuple,set)):
        print("ERROR")
    else:
        ret = iterable.pop(0)
    for i in iterable:
        ret = fn(ret,i)
    return ret

a = reduceself(fn,[1,2,3,4,5])
print(a)
# print("error") 这个换成raise 看看