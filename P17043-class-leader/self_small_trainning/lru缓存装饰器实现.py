import inspect

only_dict = dict()

def cache(fn):
    def wrapper(*args,**kwargs):
        '''
        本来用hash MD5实现
        现在根据老师讲的inspect模块实现的进阶版本
        :param args:
        :param kwargs:
        :return:
        '''
        # m = hashlib.md5()
        # arg = '{}'.format(sorted(list(args) + [v for k, v in kwargs.items()]))
        # print(arg)
        # m.update(arg.encode('utf8'))
        # md5 = m.hexdigest()
        # if md5 not in hash_dict.keys():
        #     ret = fn(*args,**kwargs)
        #     hash_dict[md5] = ret
        #     return ret
        # else:
        #     return hash_dict[md5]
        only_tuple = tuple()
        global only_dict
        sig = inspect.signature(fn)
        params = sig.parameters
        keys = params.keys()
        values = params.values()
        for i in zip(keys,args):
            only_tuple += i
        for k, v in sorted(kwargs.items()):
            only_tuple += only_tuple + (k,v)
        for k , v in sorted(params.items()):
            if v.default is not inspect._empty :
                if k not in only_tuple:
                    only_tuple += (k,v.default)
        if only_tuple in only_dict.keys():
            return only_dict[only_tuple]
        else:
            ret = fn(*args, **kwargs)
            only_dict[only_tuple] = ret
            return ret
    return wrapper


@cache
def fib(n):
    if n in (1,2):
        return 1
    return fib(n-2) + fib(n-1)


@cache
def add(x,y=2,z=10):
    return x + y + z


print(add(1,2,2))
print(add(1))
print(add(1,y=3))
print(add(z=3,y=2,x=1))
print(add(y=2,x=1,z=3))
print(add(1,y=2,z=3))
print(add(x=1,y=2,z=3))
print([fib(i+1) for i in range(35)])