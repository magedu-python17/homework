##############################
#作业1 
################################
import functools
def func1(x):
	return x*x

def func2(x,y):
		return x+y
		
def func3(x):
	return x%2==1

#################################
#作业1实现高阶函数 map filter reduce   
#################################

def map_myself(func,iterable):
	armit =iter(iterable)
	return (func(x) for x in armit)

def reduce_myself(func,iterable,initialValue=None):
	
	armit=iter(iterable) 
	value = next(armit) if initialValue is None else  initialValue
	for elemnt in armit:
		value=func(value,elemnt)
	return value

def filter_myself(func,iterable):
	armit = iter(iterable)
	return (elemnt for elemnt in armit if func(elemnt))


ret1= list(map(str,(i for i in '1234')))
ret2=list(map_myself(str, (i for i in '1234')))
ret3= list(map(func1,(i for i in range(5))))
ret4= list(map_myself(func1,(i for i in range(5))))
ret5=reduce_myself(lambda x, y : x+y,(i for i in range(5)))
ret6=functools.reduce(func2,(i for i in range(5)))
ret7=list(filter(func3,(i for i in range(1,23,3) )))
ret8=list(filter_myself(lambda x : x % 2 == 1,(i for i in range(1,23,3) )))
print(ret1,ret2,ret3,ret4,ret5,ret6,ret7,ret8,sep='\n ~~~~~~~~\n')












