#!/usr/bin/python
# -*- coding: utf-8 -*- #这是指定万国语言支持中文
#下面打印100以内的偶数
n=0
x=int(input("多少以内的:"))
for i in range(x+1):
    if i%2==0:
        n+=i
    else:
        continue
    print(n)
