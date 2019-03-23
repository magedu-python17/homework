#
# from timeit import timeit
#
# def aaa():
#     count = 0
#     while 1:
#         if count == 1000000:
#             break
#         count += 1
#
# t = timeit('aaa()', 'from __main__ import aaa', number=1)
# print(t)
# def bbb():
#     count = 0
#     while True:
#         if count == 1000000:
#             break
#         count += 1
#
# t = timeit('bbb()', 'from __main__ import bbb', number=1)
# print(t)


class Dict_(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

print(dir(dict))

A = Dict_()
A['a'] = 1
print("A", A)
print("A.a", A.a)
print("A.get(a)", A.get('a'))
print("----------")
setattr(A, 'a', 2)
print("A", A)
print("A.a", A.a)
print("A.get(a)", A.get('a'))
print(A.__dict__)

