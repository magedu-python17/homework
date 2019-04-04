#!/usr/bin/env python

import functools
import datetime
start = datetime.datetime.now()
def times(fn):
    def wrap(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        end = datetime.datetime.now() - start
        print(end.total_seconds())
        return ret
    return wrap
#@functools.lru_cache(maxsize=200)

def fi(n):
    if n < 3:
        return 1
    return fi(n-1) + fi(n-2)

print(fi(35))

end = (datetime.datetime.now() - start).total_seconds()

print("total_seconds is {:.5f}".format(end))
