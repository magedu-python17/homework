from collections import Iterable
def fn_map(x):
    return x * x
def map_self_make(fn_map,*args):
    if len(args) == 1:
        if isinstance(args[0],Iterable):
            return (fn_map(i) for i in args[0])
        else:
            print('Iterable is not Iterable')
    else:
        print('args too long,not support')
print(list(map_self_make(fn_map,[1,2,3,4,5,6])))


def fn_reduce(x):
    return x * x
def reduce_self_make(fn_reduce,*args):
    if len(args) == 1:
        if isinstance(args[0],Iterable):
            return (fn_reduce(i) for i in args[0])
        else:
            print('Iterable is not Iterable')
    else:
        print('args too long,not support')
print(list(map_self_make(fn_reduce,[1,2,3,4,5,6])))
