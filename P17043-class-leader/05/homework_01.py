from collections import Iterable

def fn_map(x):
    return x * x
def map_self_make(fn,*args):
    if len(args) == 1:
        if isinstance(args[0],Iterable):
            return (fn(i) for i in args[0])
        else:
            raise TypeError('Iterable is not Iterable')
    else:
        raise Exception('args too long,not support')
# print(list(map_self_make(fn_map,[1,2,3])))
# print(list(map_self_make(fn_map,111)))
# print(list(map_self_make(fn_map,[1,2,3],[4,5,6])))

def fn_reduce(x,y):
    return x + y
def reduce_self_make(fn,*args):
    prev = None
    if len(args) == 1:
        if isinstance(args[0],Iterable):
            for idx,item in enumerate(args[0]):
                if idx == 0:
                    prev = item
                    continue
                prev = fn(prev,item)
            return prev
        else:
            raise TypeError('Iterable is not Iterable')
    else:
        raise Exception('args too long,not support')
print(reduce_self_make(fn_reduce,[1,2,3,4]))


def fn_filter(x):
    return x % 2 == 1
def map_self_filter(fn,*args):
    # ret = []
    if len(args) == 1:
        if isinstance(args[0],Iterable):
            # for i in args[0]:
            #     if fn_filter(i):
            #         ret.append(i)
            # return ret
            return (i for i in args[0] if fn_filter(i))
        else:
            raise TypeError('Iterable is not Iterable')
    else:
        raise Exception('args too long,not support')

print(list(map_self_filter(fn_filter,[1,2,3,4,5,6,9,10,15])))

# 这个题是实现 map reduce 和filter， print 换成raise
# 可以连任 没有什么问题了


