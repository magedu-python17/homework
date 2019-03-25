#!/usr/bin/env python

def foo1(days,x=1):
    x += 1
    x *= 2
    days -= 1
    return x if days <= 1 else foo1(days,x)

print(foo1(10))
