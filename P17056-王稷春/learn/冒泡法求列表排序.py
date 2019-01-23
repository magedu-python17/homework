#!/usr/bin/python
# -*- coding: UTF-8 -*-
#利用列表的冒泡法一次打印用户输入的可排序数字:
a=[]
n=int(input("您想打印多少次数字的比较:"))
for i in range(n):
    a.append(int(input('{}:'.format(i))))
b=len(a)
for i in range(b):
    for j in range(b-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
