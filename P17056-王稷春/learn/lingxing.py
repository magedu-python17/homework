#!/usr/bin/python
# -*- coding: utf-8 -*- #这是指定万国语言支持中文 基于三元表达式打印菱形
line=int(input('>>>:'))
for i in range (-line//2,line//2+1):
    print(' '*(-i)+'*'*(line+i*2)) if i<=0 else print(' '*i+'*'*(line-i*2))
