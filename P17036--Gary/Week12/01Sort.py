#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/12/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.        
"""

# 冒泡排序   升序
lst =[98,2,4,78,12,1,6,3,10,34,55]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)

# 冒泡排序   降序
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)