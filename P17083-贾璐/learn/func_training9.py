#!/usr/bin/env python

def inc():
    print("line1")
    yield 1
    print("line2")
    yield 2
    print("line3")
    return 3


next(inc())
next(inc())
x = inc()
print(next(x))
print(next(x))
#print(next(x))
print(next(x,'End'))

