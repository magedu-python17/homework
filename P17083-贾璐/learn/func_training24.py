#!/usr/bin/env python

from functools import partial

def add(x,y,z):
    return x+y+z

newadd = partial(add,5,y = 4)

print(newadd(z = 3))
print(newadd,add)
