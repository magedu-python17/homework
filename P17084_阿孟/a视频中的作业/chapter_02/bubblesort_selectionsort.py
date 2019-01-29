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
lst = [random.randint(10,200) for _ in range(10)]
lst1 = [random.randint(10,200) for _ in range(10)]
lst2 = [random.randint(10,200) for _ in range(10)]
lst3 = [random.randint(10,200) for _ in range(10)]
lst4 = [random.randint(10,200) for _ in range(10)]
lenth1 = len(lst)
for m in range(lenth1):
    for q in range(m+1, lenth1):
        if lst[q] < lst[m]:
            lst[m], lst[q] = lst[q], lst[m]
print(lst)
#简单选择排序优化
lenth2 = len(lst1)
for i in range(lenth2):
    maxindex = i
    for j in range(i, lenth2):
        if lst1[maxindex] > lst1[j]:
            maxindex = j
    if maxindex != i:
        lst1[maxindex], lst1[i] = lst1[i], lst1[maxindex]
print(lst1)
#冒泡排序
lenth3 = len(lst2)
for s in range(lenth3):
    for w in range(lenth3-s-1):
        if lst2[w] > lst2[w+1]:
            lst2[w], lst2[w+1] = lst2[w+1], lst2[w]
print(lst2)
#冒泡排序优化：
lenth4 = len(lst3)
for t in range(lenth4-1):
    flag = False
    for tt in range(lenth4-t-1):
        if lst3[tt] > lst3[tt+1]:
            flag = True
            lst3[tt], lst3[tt+1] = lst3[tt+1], lst3[tt]
    if flag == False:
        break
print(lst3)
#插入排序
num = [0] + lst4
lenth = len(num)
for i in range(2,lenth):
    num[0] = num[i]
    j = i-1
    if num[0] < num[j]:
        while num[0] < num[j]:
            num[j+1] = num[j]
            num[j]=num[0]
            j-=1
num.remove(num[0])
print(num)
