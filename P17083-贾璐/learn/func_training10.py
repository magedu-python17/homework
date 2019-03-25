#!/usr/bin/env python

def counter():
    i = 0
    while True:
        i += 1
        yield i

def inc(c):
    return next(c)
c = counter()
print(inc(c))
print(inc(c))
print(inc(c))

