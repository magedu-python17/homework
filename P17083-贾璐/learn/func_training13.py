#!/usr/bin/env python

def counter(n):
    for i in range(n):
        yield i
def inc(n):
    yield from counter(n)

foo = inc(5)
for i in foo:
    print(i)
