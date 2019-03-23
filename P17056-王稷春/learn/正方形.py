#!/usr/bin/python
# -*- coding: utf-8 -*- #这是指定万国语言支持中文
#打印里面是空的正方形
line=int(input('>>>:'))
print('*'*line)
for i in range(line-1):
   print('*'+' '*(line-2)+'*')
print('*'*line)
