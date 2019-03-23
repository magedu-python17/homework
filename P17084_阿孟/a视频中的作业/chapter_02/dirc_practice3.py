#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-12 22:48
#
# Filename: dirc_practice3.py
#
# Description: V1.0
#
#========================================================
#
#字符串重复统计
#   在a-z字母表中挑选两个字母组成字符串组成一对，挑选100对
#   降序输出所有不同的字符串即重复次数
import random
dirc = {}
dirc2 = {}
tmplst = []
stor = 'abcdefghijklmnopqrstuvwxyz'
for s in stor:
    #dirc[s] = s
    dirc.setdefault(s)
print(dirc)
for i in range(100):
    a = ''
    for j in range(2):
        m = random.choice(list(dirc.keys()))
        a = a + m
    tmplst.append(a)
tmplst.sort()
print(tmplst)
for l in tmplst:
    dirc2.setdefault(l)
print(dirc2)
for j in dirc2:
    times = tmplst.count(j)
    print('string "{}" is repeat {} times'.format(j,times))
