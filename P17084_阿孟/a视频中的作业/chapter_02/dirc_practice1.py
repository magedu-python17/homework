#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-12 16:50
#
# Filename: dirc_practice1.py
#
# Description: V1.0
#
#========================================================
#
#用户输入一个数字
#   打印每一位及其重复的次数（数字升序排列）
from collections import OrderedDict
dirc = OrderedDict()
num = input('pls input num:')
lst = []
lenth = len(num)
for i in num:
    lst.append(i)
    lst.sort()
for s in lst:
    dirc.setdefault(s)
for j in dirc:
    dirc[j] = lst.count(j)
    print('Number {} is repeat {} times.'.format(j,dirc[j]))
