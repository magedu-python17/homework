#!/usr/bin/env python

def cache(fn):
    local_cache = {}
    def _cache(*args,**kwargs):
        key = args
        value = tuple([x for x in kwargs.values()])
        keys = key + value

        #查询与缓存
        if key != () and value == () and key not in local_cache.keys():
            local_cache[key] = fn(*args,**kwargs)
        elif key == () and value != () and value not in local_cache.keys():
            key = value
            local_cache[key] = fn(*args,**kwargs)
        elif key != () and value!= () and keys not in local_cache.keys():
            key = keys
            local_cache[key] = fn(*args,**kwargs) 
        return local_cache[keys]
    return _cache

@cache

def fn(x,y):
    return x+y


print(fn(1,2))
print(fn(x=1,y=2))
print(fn(1,y=2))

