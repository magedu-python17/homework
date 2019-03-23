#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-12 22:48
#
# Filename: dirc_practice2.py
#
# Description: V1.0
#
#========================================================
#
#数字重复统计
#   随机产生100个数,范围[-1000,1000]
#   升序排列所有不同的数字与重复次数
import random
from collections import OrderedDict
dirc = OrderedDict()
lst = []
for i in range(100):
    num = random.randint(-1000,1000)
    lst.append(num)
lst.sort()
for s in lst:
    dirc.setdefault(s)
for j in dirc:
    dirc[j] = lst.count(j)
    print('Number {} is repeat {} times.'.format(j,dirc[j]))
