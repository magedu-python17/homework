#!/usr/bin/python
# -*- coding: UTF-8 -*-
#计算三个数大小排序:使用max函数打印出来
num=[]
n=int(input("您想打印多少次:"))
for i in range(n):
    num.append(int(input("{}:".format(i))))
num.sort()
print(num)
