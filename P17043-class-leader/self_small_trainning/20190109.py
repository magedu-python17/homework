#
# lst = [1,2,3,4]
# aaa = ','.join(map(str,lst))
# print(aaa)
# print(type(aaa))
#
# lst2 = 'ddd\r\n\nqfre\n    222'.splitlines()
# print(lst2)
#
# lst3 = 'a,b,c,d'.partition('c')
# print(lst3)
#
# print('a asss b'.upper().lower().split())
#
# print('ffffffffffffffffffffffffffff'.center(100,'#'))
#
# s = ' I am very very very sorry '
# print(s.strip(' syrrveo'))


# s = '/etc/apache.conf'
# print(s.endswith('conf'))


# def run():
#     return lambda : print('aaa')
#
# a = run()
# print(a)
# a()
#
# def guyuanjun():
#     print('heheh')
# guyuanjun()
#
# guyuanjun = lambda : print('heheh')
# guyuanjun()


# a =b'a'
# print(a)
# print(a[0])
#
#
# for x in 'a'.encode('ascii'):
#      print(x)

# def counter():
#     c = [0]
#     def inner():
#         c.append(6)
#         return c
#     return inner
# foo = counter()
# print(foo(),foo())
# print(foo())

# def create_multipliers():
#     ret = []
#     for i in range(5):
#         def aaa(x):
#             return i*x
#         ret.append(aaa)
#     return ret
#
# for multiplier in create_multipliers():
#     print(multiplier(4))
#
#
# print([i for i in range(5)])
# print('******************************')
# a = [lambda x : 0 * x ,lambda x : 1 * x,lambda x : 2 * x,lambda x : 3 * x,lambda x : 4 * x,lambda x : 5 * x ]
# for i in a:
#     print(i(4))
#
#
# print(list(range(2,2)))


#给一个数，判断它是否是素数（质数）
num = int(input("Input a number: "))
for i in range(2,num):
    if num % i == 0:
        print('NO')
        break
else:
    print('Yes')