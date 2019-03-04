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
