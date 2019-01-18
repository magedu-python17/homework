#!/usr/bin/python
# -*- coding: UTF-8 -*-
#先写第一种:
m=[[1],[1,1]]
n=int(input("您想打印多少次杨辉三角:"))
for i in range(2,n):
    y=[1]
    x=m[i-1]
    for j in range(i-1):
        pre=x[j]+x[j+1]
        y.append(pre)
    y.append(1)
    m.append(y)
print(m)


#第二种:
n=int(input("您想打印多少次:"))
a=[1]
b=[1,1]
print(a)
print(b)
for i in range(2,n):
    x=[1]
    for j in range(i-1):
        y=b[j]+b[j+1]
        x.append(y)
    x.append(1)
    print(x)
    b=x   #这最后一次是数值替换更新 

