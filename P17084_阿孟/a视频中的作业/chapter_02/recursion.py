#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-03-01 22:52
#
# Filename: recursion.py
#
# Description: V1.0
#
#========================================================
#猴子吃桃循环定义
def monkey(n,s=1):
    for _ in range(n-1):
        s = (s + 1) * 2
    return s
print(monkey(10))
#猴子吃桃递归定义
def monkey(day):
    if day == 1:
        return 1
    return (monkey(day-1)+1) * 2
print(monkey(10))
#阶乘递归定义
def fac(num):
    if num == 1:
        return 1
    return num * fac(num - 1)
print(fac(5))
#阶乘循环定义
def fac1(num,s=1):
    for i in range(1,num+1):
        s = s * i
    return s
print(fac1(5))
