#!/usr/bin/env python

import functools

def logger(fn):
    @functools.wraps(fn)
    def wrap(*args,**kwargs):
        print("This is a wrap")
        ret = fn(*args,**kwargs)
        return ret
    return wrap

@logger

def add(x,y):
    return x+y

print(add.__name__)
