# print(
#     list(
#         zip(
#             ('a','b','c','d','e'),(1,2,3,4,5)
#         )
#     )
# )


# if (1 in [1, 0]) and ([1, 0] == False):
if 1 not in [1,0] == False:
    print('铁匠')
else:
    print('原凯')

# 理解都没有错，但是实际上是这样运行的：
# 1 in [1, 0] == False  可以转为 (1 in [1, 0]) and ([1, 0] == False)
# 类似 a < b < c  可以转为 (a<b) and (b< c)


from collections import namedtuple

a = [1,2,3,4]
print(list(map(str,a)))

Point = namedtuple('P','name,age')
p = Point('xiayang',18)
print(p.name,p.age)

