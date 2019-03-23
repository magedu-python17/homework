# -*- coding: UTF-8 -*-
#计算三个数大小排序:使用max函数打印出来
num=[]
n=int(input("您想打印多少个值的大小排序:"))
for i in range(n):
    num.append(int(input('{}:'.format(i))))
while True:
    x=max(num)
    print(x)
    num.remove(x)
    if len(num)==1:
        print(num[0])
        break
