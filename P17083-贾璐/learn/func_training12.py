#!/usr/bin/env python

def inc():
    x = 0
    y = 1
    while True:
        yield y
        x,y = y,x+y

x = inc()
for i in range(10):
    print(next(x))
