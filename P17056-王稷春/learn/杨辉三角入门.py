#!/usr/bin/python
# -*- coding: UTF-8 -*-
a=[[1],[1,1]]   #前面的给他固定次数
n=int(input("您想打印多少次杨辉三角:"))   #交互式体验
for i in range(2,n):  #$让i的取值先去掉前面两次
    b=[1]     #定义新的元素的第一个值
    pre = a[i-1]    #因为如果是从2开始则需要减一不然就有两个取值了  不对 应该只有一个取值 就是取a的元素为1来作为元素2的运算基数
    for j in range(i-1):    #让它的循环次数再减一 目的是从第一个新的元素开始每次循环都是上次元素总数减一个 这样才能构成三角
        val=pre[j]+pre[j+1]   #这个val的取值是一个个数 是pre列表里面的元素的运算得出的值
        b.append(val) # 将val循环之后的计算出的得数追加到b里面 这里为什么不用insert 和remvoe呢 因为列表大了之后不好运算 对于内存消耗较大 所以最好不用 而追加则是很方便的
    b.append(1) #将循环之后的列表最后再加一 这个是最外层的一
    a.append(b)  #将b的整个列表作为元素追加到a这个大列表中去 这个是列表套列表的方法
print(a) #最后输出a



#关于杨辉三角的学习第一遍:
#这个时候i的取值直接影响到了列表的循环次数 每次取值都是一次列表的总数 这样后面的取值就是上次的所有的相加了 不懂得则多写几遍
# -*- coding: utf-8 -*- #这是指定万国语言支持中文 基于三元表达式打印菱形
n=6
print([1])
pre=[1,1]
print(pre)
for i in range(2,n):
    b=[1]
    for j in range(i-1):
        val=pre[j]+pre[j+1]
        b.append(val)
    b.append(1)
    print(b)
    pre=b #将pre替换为b 这样下次再打印的时候又可以和它一样了
#这里用到的是列表加数值转换 像以前的斐波那数列一样
# -*- coding: UTF-8 -*-
#打印杨辉三角
n=int(input("您想打印多少次杨慧三角:"))
x=[1]
print(x)
y=[1,1]
print(y)
for i in range(2,n):
    b=[1]
    for j in range(i-1):
        pre=y[j]+y[j+1]
        b.append(pre)
    b.append(1)
    print(b)
    y=b
 
