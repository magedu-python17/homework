
# 冒泡排序
# num_list = [1,9,8,5,6,7,4,3,2,120,1398,2000,12,456,800,0,98,178,123,156,76]
# num = len(num_list)
# a = 0
# for i in range(num):
#
# 	for j in range(num-1):
# 		if num_list[j] >num_list[j+1]:
# 			print(a)
# 			a +=1
# 			num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
#
# print(num_list)
# print(a)





# 打印杨辉三角
# n = 6
# row =[1]*n
#
# for i in range(6):
# 	offset = n-i
# 	z = 1
# 	for j in range(1,i//2+1):
# 		val = z + row[j]
# 		row[j],z = val,row[j]
# 		if i!=2*j:
# 			row[-j-offset] = val
# 	print(row[:i+1])


# 字符串的联系
# 判断几位数
# 打印每一位数字出现的次数
#

# 判断几位数
# num = input("请输入数字:>>")
# length = len(num)
# # print(length)
#
# # 打印每个数出现的次数
# for i in range(10):
# 	z = num.count(str(i))
# 	if z!=0:
# 		pass
# 		# print(z)
#
# lst = list(num)
# # print(lst)
# for i in range(length):
# 	print(lst[-1+int(-i)])
# 	# print(type(i))


# 输入五个数，并排序
# ls = []
# for i in range(5):
# 	ls.append(int(input("请输入一个数:")))
#
# print(ls)
#
# # ls.sort(reverse=False)
# # sorted(ls,reversed=True)
# sorted(ls)
# print(ls)

# 矩阵逆转’
# l1=[1,2,3]
# l2 = [4,5,6]
# l3=[7,8,9]
# lst = [l1,l2,l3]
# lst1= []
# lst2 =[]
# print(lst)
# for i in range(3):
# 	for j in range(3):
# 		lst1.append(lst[j][i])
# 	lst2.append(lst1)
# 	# print("\n")
# print(lst2)


# 随机产生10个是，范围0-20，并统计个数
# import random
# lst = []
# for i in range(10):
# 	temp = random.randint(1,20)
# 	lst.append(temp)
# print(lst)

# 求出现的次数
# for i in range(20):
# 	cnt = lst.count(int(i))
# 	if cnt !=0:
# 		# print(cnt)
# 		if cnt ==1:
# 			print('数字%d出现了%d次' %(i,cnt))
# 		else:
# 			print('数字%d出现了%d次' %(i,cnt))



# 封装及解封
# a = 1,2,3
# print(a)
# print(type(a))

# x,y = 1,2
# x,y = y,x
# print(x,y)
# x,y="ab"
# print(x,y)




# (a,*b)= {20,30,40}
#
# print(type(a))
# print(type(b))
# print(a,b)


# lst = list(range(1,101,2))
# head,*mid,tail = lst
# print(head,tail)
# print(type(head),type(tail))
# print(mid)
# print(type(mid))


# tail, *xxx=[1,2]
# print(tail)
# print(xxx)

# 给一个列表取出2,4,8的数
# lst = list(range(1000))
# print(lst)
# head,*mid,tail =lst
# print(head,tail)
# print(mid[0],mid[2],mid[-1])
#
# _,a,_,b,*_,c,_ = lst
# print(a,b,c)

# 取最后一个元素
# ls = [1,(2,3,4),5]
# _,(*_,val),*_=ls
# print(val)

# 提取环境变量
# key,_,val = "JAVA_HOME=/usr/bin".partition('=')
# print(key)
# print(val)

# s3 = set(list(range(10)))
# print(s3)
# print(type(s3))
#
# s6 = {(1,2),3,'a'}
# print(s6)
# print(type(s6))

# s7 = {[1],(1,),1}
# print(s7)
# print(type(s7))

# print(hash(0b1110))
#
# print(hash('abcdefgh'))
#
# print(hash('abcdefghg'))


# 选择排序
# lst = [1,9,8,5,6,7,4,3,2]
# length = len(lst)
#
# for i in range(length):
# 	x = lst[i]
# 	maxindex = i    # 最大索引
# 	for j in range(i+1,length):
# 		if lst[j] >lst[i]:
# 			maxindex = j
# 			pass

# 时间模块
# import time
#
# print(time.altzone)
# print(time.time())
# print(time.ctime())
# print(time.)

# 导入时间模块
# import datetime
# # print(datetime.today())
# # 获取当前时间
# print(datetime.datetime.now())
# print(datetime.datetime(2018,11,24))
# print(datetime.datetime.isoweekday)

# g = ("{:04}".format(i) for i in range(1,11))
# next(g)
# print(type(g))
# for x in g:
# 	print(x)
# print('~~~~~~~~~~~~~~~~~')
# for x in g:
# 	print(x)

# g = ["{:04}".format(i) for i in range(1,11)]
# for x in g:
# 	print(x)
# print('~~~~~~~~~~~~~~~~~')
# for x in g:
# 	print(x)

# it = (print("{}".format(i+1)) for i in range(2))
# first = next(it)
# print(first)
# # print(type(first))
# sceond = next(it)
# # val = first + sceond
# # print(val)
# # print(type(val))

# g = {(x,) for x in range(10)}
# print(g)
# print(type(g))

# g ={chr(0x41+x):x**2 for x in range(10)}
# print(g)
#

# # 为什么输出3个
# s = {str(x):y for x in range(3) for y in range(4)}
# print(s)

# # 递归的深度
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)

# import itchat
# from itchat.content import *
# # 扫描登录微信
# itchat.auto_login(hotReload=True)
# itchat.send(u'测试消息发送','filehelper')

#文件拷贝
# import shutil
# shutil.copyfileobj(src,dst)

# import msgpack
# # import json
# d = dict(zip('abcde',[None,True,False,[1,'abc'],{'a':1,'b':2}]))
# b1 = msgpack.dumps(d)

# print(len(b1),type(b1))
# print(b1)

# ret = msgpack.unpackb((b1))
# print(ret)

# import argparse

# parser = argparse.ArgumentParser()
# print(parser)

# line = "140.205.201.44 - - [07/Apr/2017:08:11:06 +0800] "GET / HTTP/1.1" 200 8642 "http://job.magedu.com/" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;Alibaba.Security.Heimdall.950384.p)""

# class Person:
# 	"""文档的字符串"""   #类属性
# 	x = 'abc'
# 	def __init__(self,name):
# 		self.name = name
# 		self.age = 18
# print(Person.x)
# # print(Person.age)
# # print(Person.name)
# p = Person('molson')
# print(p.name)
# print(p.age)
# print(Person.__doc__)


# class Person:
#
# 	@classmethod
# 	def normal_function(cls):
# 		print('normal function')

# # Person.normal_function()
# # Person().normal_function()
# print(Person.__dict__)
import time
# 类的定义
# class Student:
# 	def __init__(self,name):
# 		self._name = name
# 		# self._scores = kwargs
#
# 	# @property
# 	def get_score(self):
# 		return self._scores
#
# 	@property
# 	def name(self):
# 		return self._name

# 	def __del__(self):
# 		print('del')
# tom = Student('tom')
# # print(tom.get_score())
# jerry = Student('Jerry')
#
# # del tom
# print('~~~~~~')
# time.sleep(3)
#
# print(tom.name)
# # del jerry
# print('=====and=======')

# class Animal:
# 	def __init__(self,name):
# 		self._name = name
# 	@property
# 	def name(self):
# 		return self._name
#
# 	def shout(self):
# 		print('{}.{} shouts'.format(self.__class__.__name__,self.name))
#
# class Cat(Animal):
# 	def __init__(self,name):
#
# 		print('cat')
# 		pass
# 	# def shout(self):
# 	# 	print('Mao shouts')
# 	pass
#
# class Dog(Animal):
# 	pass
#
# a = Animal('monster')
# print(Animal.__dict__)
# print(Cat.__dict__)
# print(Dog.__dict__)
# a.shout()
#
# c = Cat('garfield')
# c.shout()
# d = Dog('ahuang')
# d.shout()

# print(int.__mro__)   #显示方法的查找顺序
# print(int.mro())     #显示方法的查找顺序
# print(int.__bases__)  #类的基类元祖
# print(int.__base__)  #类的基类
# print(int.__subclasses__())   #类的子类

# import random
# class Sranders:
# 	def __init__(self,start=1,stop =100,count=10):
# 		self.start = start
# 		self.stop = stop
# 		self.count = count
#
# 	def genter(self,start=1,stop =100,count =10):
# 		return [random.randint(self.start,self.stop) for x in range(self.count)]
# ret = Sranders(1,100,20)

# class Point:
# 	ls = []
# 	def __init__(self,x,y):
# 		self.x = x
# 		self.y = y
#
# 	def Rec(self):
# 		for i in range()
# print(ret.genter())

# class Car:
# 	def __init__(self,name,color,price,speed):
# 		self.name = name
# 		self.color = color
# 		self.price = price
# 		self.speed = speed
#
# class Info:
# 	def __init__(self):
# 		self.info = []
#
# 	def add(self,ca):
# 		self.info.append(ca)
#
# 	def show(self):
# 		return (self.info)
# car = Car('宝马','红色',198,200)
# L =Info()
# L.add(car)
# l1 =L.show()
# print(l1)
# print(type(l1))
# for i in l1:
# 	print(i)


# 实现温度的转换
# class ChangeTemp:
# 	def __init__(self,num):
# 		self.num = num
#
# 	def ChangeToH(self):
# 		return 9*(self.num/5)+32
#
# 	def ChangeToS(self):
# 		return 5*(self.num-32)/9
#
# 	def ChangToK(self):
# 		return self.num + 273.5
# t = ChangeTemp(100)
# print('华氏温度',t.ChangeToH())
# print('摄氏温度',t.ChangeToS())
# print('开氏温度',t.ChangToK())


class A:
	def __init__(self,a):
		self.a = a

class B(A):
	def __init__(self,b,c):
		self.b = b
		self.c = c
		A.__init__(self,b+c)

	def printv(self):
		print(self.b,self.c)
		print(self.a)

b = B(4,5)
b.printv()

print(b.__dict__)
# print(B.__dict__)
# print(A.__dict__)







