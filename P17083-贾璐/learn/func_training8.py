#!/usr/bin/env python

def inc():
    for i in range(5):
        yield i

print(type(inc))
print(type(inc()))

x = inc()
print(next(x))
for m in x:
    print(m,'*')
for m in x:
    print(m,'**')
