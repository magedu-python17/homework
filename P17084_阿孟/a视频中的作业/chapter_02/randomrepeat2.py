#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-10 19:21
#
# Filename: randomrepeat2.py
#
# Description: V1.0
#
#========================================================
#
import random
lst = []
lst1 = []
seter = set()
n = 0
for i in range(10):
    lst.append(random.randint(10,20))
print('list1: {}'.format(lst))
for s in range(10):
    lst1.append(random.randint(10,20))
print('list2: {}'.format(lst1))
seter.update(lst,lst1)
lst3 = lst + lst1
for t in seter:
    tms = lst3.count(t)
    if tms == 1:
        print('{} is norepeat.'.format(t))
    else:
        repeatnum = t
        tms2 = tms
        print('{} is repeat {} times.'.format(repeatnum,tms2))
