#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-08 23:39
#
# Filename: sort3.py
#
# Description: V1.0
#
#========================================================
#
#用户输入一个数字
#	1.判断是几位数
#	2.打印每一位数字及其重复的次数
#	3.从低位到高位打印数字
#
num = int(input())
lst = list(str(num))
#print(lst)
lenth = len(str(lst))
n = 0
lst2 = []
for s in lst:
    if s not in lst2:
        lst2.append(s)
for i in lst2:
    tim = lst.count(lst2[int(n)])
    print(lst2[int(n)],'--->',tim,'times')
    n+=1
    #print(tim)
print('The number is',len(str(num)),'bytes')
lst.reverse()
print(''.join(lst))
