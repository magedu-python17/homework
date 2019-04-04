#!/usr/bin/env python

from inspect import signature
import functools


def functype_check(fn):
    @functools.wraps(fn)
    def wrap(*args,**kwargs):
        sig = signature(fn)
        params = sig.parameters
        keys_list = list(params.keys())
        values_list = list(params.values())
        for i,item in enumerate(args):
            if isinstance(item,values_list[i].annotation):
                print(keys_list[i], '==',item)
        for k,v in kwargs.items():
            if isinstance(v,params[k].annotation):
                print(k,"===",v)
        ret = fn(*args,**kwargs)
        return ret
    return wrap

@functype_check
def add(x:int,y:int,*args,**kwargs):
    return x+y


print(add(x = 4,y = 5))

