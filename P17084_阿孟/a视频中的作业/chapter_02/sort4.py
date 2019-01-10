#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-09 12:59
#
# Filename: sort4.py
#
# Description: V1.0
#
#========================================================
#
#用户输入一个数字
#   1.判断是几位数
#   2.打印每一位数字及其重复的次数
#   3.从低位到高位打印数字
#
num = int(input('>>>'))
lst = list(str(num))
lenth = len(str(lst))
n = 0
lst2 = []
for s in lst:
    if s not in lst2:
        lst2.append(s)
for i in lst2:
    print('{}--->num={}'.format(lst2[int(n)],lst.count(lst2[int(n)])))
    n+=1
print('输入的数字是{}位'.format(len(str(num))))
lst.reverse()
print('从低位到高位排列--->{}'.format(''.join(lst)))
