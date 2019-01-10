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
    i = random.randint(10,20)
    lst.append(i)
print('list1: {}'.format(lst))
for s in range(10):
    s = random.randint(10,20)
    lst1.append(s)
print('list2: {}'.format(lst1))
seter.update(lst,lst1)
lst3 = lst + lst1
#print(lst3)
#print('The random list is {}.'.format(seter))
for t in seter:
    tms = lst3.count(t)
    #print(tms)
    if tms == 1:
        print('{} is norepeat.'.format(t))
    else:
        repeatnum = t
        tms2 = tms
        print('{} is repeat {} times.'.format(repeatnum,tms2))
