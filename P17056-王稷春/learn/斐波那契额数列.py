#!/usr/bin/python
# -*- coding: utf-8 -*- #这是指定万国语言支持中文
#打印一百以内的菲波那切数列
a=1
b=1
while b<100:
    print(b)
    a,b=b,a+b

a=1
b=1
n=int(input("您想打印多少次:"))
for i in range(n):
    print(b)
    a,b=b,a+b

