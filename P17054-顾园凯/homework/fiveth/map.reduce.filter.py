from collections import Iterable


def map(fn, iterable):

    if isinstance(iterable, Iterable):
        return (fn(x) for x in iterable)
    else:
        return 'iterable is not iterable'


def fn(x):
    return x * x


ret = list(map(fn,[1,2,3,4,5,6,7,8,9]))
str1 = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(ret)
print(str1)


def reduce(fn,iterable):
    if isinstance(iterable, Iterable):
        sum = 0
        for i in iterable:
            sum = fn(sum, i)
        return sum
    else:
        return 'iterable is not iterable'


def fn(x, y):
    return x+y


ret = reduce(fn,[1, 3, 5,7, 9])
print(ret)


def filter(fn,iterable):
    if isinstance(iterable, Iterable):
        return (i for i in iterable if fn(i))
    else:
        return 'iterable is not iterable'


def fn(n):
    return n % 2 == 1


ret = list(filter(fn, [1,2, 4, 5, 6, 9, 10, 15]))
print(ret)


