#!/usr/bin/env python

def counter():
    a = [2]
    def co():
        a.append(4)
        print(a)
        return a
    return co



a = counter()
print(a(),a())
