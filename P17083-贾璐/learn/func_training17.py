#!/usr/bin/env python



def logger(fn):
    def _logger(*args,**kwargs):
        print(1)
        ret = fn(*args,**kwargs)
        print(2)
        return ret
    return _logger

@logger
def add(x,y,*,z=6):
    return x+y+z


r = add(1,3,z=7)
print(r)
