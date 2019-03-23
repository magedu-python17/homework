#!/usr/bin/python
from collections import namedtuple


student=namedtuple('stu','name age')
s1=student('tom',29)
s2=student('jerry',18)
print(s1)
print(s2)

a = namedtuple('x',['name','age','sex'])
b = a('wangjichun',23,175)
c = a('wangshinuo',23,162)
print(b)
print(c)
print(b.name)



test=namedtuple('test','age name sex shenggao')
new=test(12,'zhang',24,176)
xinjian=test(13,'zhou',34,167)
z=test(14,'zhpou',34,567)
print(new)
print(xinjian)
print(z)
w=tuple(range(10))
print(w)
