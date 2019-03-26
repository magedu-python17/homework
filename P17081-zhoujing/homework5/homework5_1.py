from collections.abc import Iterable
##############################
# 作业1
################################
import functools


def func1(x):
	return x * x


def func2(x, y):
	return x + y


def func3(x):
	return x % 2 == 1


#################################
# 作业1实现高阶函数 map filter reduce
#################################

def map_myself(func, iterable):
	if isinstance(iterable,Iterable):
		armit = iterable
		return (func(x) for x in armit)
	else:
		raise TypeError('only use iterable obj')


def reduce_myself(func, iterable, initialValue=None):
	if isinstance(iterable, Iterable):
		armit = iter(iterable)
		value = next(armit) if initialValue is None else initialValue
		for elemnt in armit:
			value = func(value, elemnt)
		return value
	else:
		raise TypeError('only use iterable obj')


def filter_myself(func, iterable):
	if isinstance(iterable, Iterable):
		armit = iter(iterable)
		return (elemnt for elemnt in armit if func(elemnt))
	else:
		raise TypeError('only use iterable obj')


ret1 = list(map(str, (i for i in '1234')))
ret2 = list(map_myself(str, (i for i in '1234')))
ret3 = list(map(func1, (i for i in range(5))))
ret4 = list(map_myself(func1, (i for i in range(5))))
ret5 = reduce_myself(lambda x, y: x + y, (i for i in range(5)))
ret6 = functools.reduce(func2, (i for i in range(5)))
ret7 = list(filter(func3, (i for i in range(1, 23, 3))))
ret8 = list(filter_myself(lambda x: x % 2 == 1, (i for i in range(1, 23, 3))))
print(ret1, ret2, ret3, ret4, ret5, ret6, ret7, ret8, sep='\n ~~~~~~~~\n')

# 写的很好，如果能把这些的高阶函数的用法，再理一遍的话，那就更好了




