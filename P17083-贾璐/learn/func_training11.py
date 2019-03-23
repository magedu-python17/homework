#!/usr/bin/env python


def inc():
    def counter():
        i = 0
        while True:
            i += 1
            yield i
    c = counter()
    return lambda :next(c)

foo = inc()
print(foo())
print(foo())
