#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-13 23:37
#
# Filename: bubblesort_selectionsort.py
#
# Description: V1.0
#
#========================================================
import random
from collections import OrderedDict
dirc = OrderedDict()
lst = []
lst1 = []
lst2 = []
lst3 = []
for i in range(20):
    num = random.randint(-1000,1000)
    lst.append(num)
    lst1.append(num)
    lst2.append(num)
    lst3.append(num)
#简单选择排序：
lenth1 = len(lst)
for m in range(lenth1):
    for q in range(m+1,lenth1):
        if lst[q] < lst[m]:
            lst[m],lst[q] = lst[q],lst[m]
print(lst)
#简单选择排序优化
lenth2 = len(lst1)
for i in range(lenth2):
    maxindex = i
    for j in range(i,lenth2):
        if lst1[maxindex] > lst1[j]:
            maxindex = j
    if maxindex != i:
        lst1[maxindex],lst1[i] = lst1[i],lst1[maxindex]
print(lst1)
#冒泡排序
lenth3 = len(lst2)
for s in range(lenth3):
    for w in range(lenth3-s-1):
        if lst2[w] > lst2[w+1]:
            lst2[w],lst2[w+1] = lst2[w+1],lst2[w]
print(lst2)
#冒泡排序优化：
lenth4 = len(lst3)
for t in range(lenth4-1):
    flag = False
    for tt in range(lenth4-t-1):
        if lst3[tt] > lst3[tt+1]:
            flag = True
            lst3[tt],lst3[tt+1] = lst3[tt+1],lst3[tt]
    if flag == False:
        break
print(lst3)
