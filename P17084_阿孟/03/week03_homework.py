#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-14 21:16
#
# Filename: week03_homework.py
#
# Description: V1.0
#
#========================================================
#
#第三次的作业：
#  s = "Sorting1234" 
#给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
#1 所有的小写字母在大写字母前面
#2 所有的字母在数字前面
#3 所有的奇数在偶数前面 
#=========================
#还未学到函数，所以用比较笨的方式完成
while 1:
    lst = str(input('pls input num or letter:'))
    oddlst = []
    evenlst = []
    letter = []
    if lst == 'stop':
        break
    for i in lst:
        if ord(i) <= 57 and ord(i) >= 48:
            if not int(i) % 2:
                evenlst.append(i)
            else:
                oddlst.append(i)
        else:
            letter.append(i)
        evenlst.sort()
        oddlst.sort()
        letter.sort(reverse=True)
    print(''.join(letter + oddlst + evenlst))
    oddlst.clear()
    evenlst.clear()
    letter.clear()
