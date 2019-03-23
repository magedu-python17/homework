#!/usr/bin/python
# -*- coding: UTF-8 -*-
#杨辉三角
#三个数比大小
#先算第一题：
n=int(input("想打印多少次:"))
a=[1]
b=[1,1]
print(a)
print(b)
for i in range(2,n):
    x=[1]
    for j in range(i-1):
        pre=b[j]+b[j+1]
        x.append(pre)
    x.append(1)
    print(x)
    b=x



#再算第二题:
a=[[1],[1,1]]
n=int(input("想打印多少次:"))
for i in range(2,n):
    x=[1]
    y=a[i-1]
    for j in range(i-1):
        pre=y[j]+y[j+1]
        x.append(pre)
    x.append(1)
    a.append(x)
print(a)


#分支结构计算分数:
a=int(input("请输入第一个数:"))
b=int(input("请输入第二个数:"))
c=int(input("请输入第三个数:"))
if a >=b:
    if a>=c:
        if b>=c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if c>=b:
        print(c,b,a)
    else:
        if a>=c:
            print(b,a,c)
        else:
            print(b,c,a)
