#!/usr/bin/env python
import datetime
import time
def logger(fn):
    def wrap(*args,**kwargs):
        print("args = {}, kwargs = {}".format(args,kwargs))
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        end = datetime.datetime.now() - start
        print("func {} took {}s".format(fn.__name__,end.total_seconds()))
        return ret
    return wrap

@logger

def add(x,y):
    print("==============call add==================")
    time.sleep(2)
    return x+y

print(add(4,y=7))
