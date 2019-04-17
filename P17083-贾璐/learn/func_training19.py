#!/usr/bin/env python

import datetime
import time

def func_name(src):
    def wrap(dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest
    return wrap



def logger(duration,func=lambda name,end:print(name,end)):
    def _logger(fn):
        @func_name(fn)
        def wrap(*args,**kwargs):
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            time.sleep(5)
            end = datetime.datetime.now() - start
            print("{} is too slow.".format(fn.__name__)) if end.total_seconds() > duration else print("{} is fast.".format(fn.__name__))
            func(fn.__name__,end.total_seconds())
            print("fn name is {0},{0}'s time is {1}".format(fn.__name__,end.total_seconds()))
            return ret
        return wrap
    return _logger

@logger(5,func=lambda name,end:print(name) if end > 5 else print(end.total_seconds()))

def add(x,y):
    """This is a doc
        example:
            add(4,56)
    """
    return x + y

print(add(45,56))
print("name is {} \ndoc = {}".format(add.__name__,add.__doc__))
