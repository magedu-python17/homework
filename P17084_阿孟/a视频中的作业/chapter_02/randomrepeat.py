#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-09 22:11
#
# Filename: randomrepeat.py
#
# Description: V1.0
#
#========================================================
import random
lst = []
lst2 = []
n = 0
for i in range(10):
    i = random.randint(1,20)
    lst.append(i)
print('The random list is {}.'.format(lst))
for j in lst:
    if j not in lst2:
        lst2.append(j)
for t in lst2:
    tms = lst.count(lst2[n])
    if tms == 1:
        noreindex = n
        print('{} is norepeat.'.format(lst2[noreindex]))
    else:
        repeat = tms
        reindex = n
        print('{} is repeat {} times.'.format(lst2[reindex],repeat))
    n += 1
