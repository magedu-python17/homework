#!/usr/bin/python
# -*- coding: utf-8 -*- #这是指定万国语言支持中文
a=int(input("请输入您想打印的素数的最小值范围:"))
b=int(input("请输入您想打印的素数的最大值范围:"))
for i in range(a,b+1):
    if i >1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

#python里面 /表示精确除法 //表示取整数

