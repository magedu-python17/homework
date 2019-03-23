#!/usr/bin/python
n=int(input("你想打印多少个数的列表集合:"))
x=[]
for i in range(n):
    x.append(int(input("{}:".format(i))))
a=len(x)
for j in range(a):
    for k in range(a-1-j):
        if x[k]>x[k+1]:
            x[k],x[k+1]=x[k+1],x[k]
print(x)
