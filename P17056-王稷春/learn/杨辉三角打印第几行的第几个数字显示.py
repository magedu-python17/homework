#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=[1]
b=[1,1]
n=int(input("您想显示多少行:"))
p=int(input("情输入您想显示的行对应的索引号:"))
if n<p:
    print("您所想打印的行号{}对应的第{}数字不存在!".format(n,p))
else:
    for i in range(2,n):
        m=[1]
        for j in range(i-1):
            x=b[j]+b[j+1]
            m.append(x)
        m.append(1)
        b=m
    print(b)
    print("您想显示的第{}行的第{}个数字是{}".format(n,p,b[p]))
