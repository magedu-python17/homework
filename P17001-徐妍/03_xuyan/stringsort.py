#小写大写奇数偶数
#s = 'XY44tcTC20130767'
s = input('>>>please input a string:')
print(''.join( sorted(s,key = lambda c:(c.isdigit(),c.isdigit() and int(c) % 2 ==0,c.isupper()))))


# 没有问题，这样写的逻辑，最好书写出来



