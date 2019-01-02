#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__mtime__ = '2019/1/2'
# code is far away from bugs with the god animal protecting，I love animals.
"""
import time
import random
# 给定一个只包含大小写字母，数字的字符串，对其进行排序
# 1：所有小写字母在大小字母后面
# 2：所有的字母在数字前面
# 3: 所有的基数在偶数前面
#例如
s = 'Sorting1234'

# 请用户输入一个字符串
st = input('请输入一个字符串，包括大小写字母及数字>>')

# 分开字母和非数字列表
def list_ls(st):
    ret = len(st)
    print('排序前的字符串为......')
    print(st)
    #定义三个字符串，分别存放大写字母，小写字母及数字
    ss_lowstr  = ''
    ss_uperstr = ''
    str_number = ''
    for i in st:
        if i>= str(0) and i <= str(9):
           str_number += i
        else:
            if i.islower():
                ss_lowstr += i
            else:
                ss_uperstr += i

    #分表调用三个相关函数进行排序
    s1_lowstr = sort_lowstr(ss_lowstr)
    s1_uperstr = sort_uperstr(ss_uperstr)
    s1_number = srot_number(str_number)

    time.sleep(random.randint(1,3 if ret>30 else 10))
    #排序后的字符串为
    after_str = s1_uperstr +s1_lowstr+s1_number
    print('排序后的字符串顺序为........')

    print(after_str)

# str_number = '13579204'
# 数字字符串转换成按照
def srot_number(str_number):
    # 定义两个字符串分别存放基数和偶数
    s1 = []
    s2 = []
    for i in str_number:
        if int(i)%2 ==0: #偶数
            # print(i)
            s1.append(int(i))
        else:  #基数
            # print('pass')
            s2.append(int(i))

    # 对基数偶数进行排序
    s1.sort()
    s2.sort()

    # 把两个列表转换字符串并连接
    ss = ''  #定义一个空的字符串
     # 把列表转换成字符串
    for i in s2:
        ss += str(i)

    # 把列表转换成字符串
    for i in s1:
        ss +=str(i)

    return ss


# 对字符串进行排序
# 小写字母进行排序
# ss_loustr = 'qwertyuiopasdfghjklzxcvbnm'
def sort_lowstr(ss_loustr):
    s1 = []
    for i in ss_loustr:
        s1.append(i)

    s1.sort()

    s2 = ''
    for i in s1:
        s2 +=i

    return s2


# 大写字母进行排序
# ss_uperstr = 'QWERTYUIOPASDFGHJKLZXCVBNM'
def sort_uperstr(ss_uperstr):
    s1 = []
    for i in ss_uperstr:
        s1.append(i)

    s1.sort()

    s2 = ''
    for i in s1:
        s2 +=i

    return s2

if __name__ == '__main__':
    list_ls(st)