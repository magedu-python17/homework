#!/usr/bin/env python

def foo1(n,num = 1):
    num *= n
    return num if n <= 1 else foo1(n-1,num)
print(foo1(5))
