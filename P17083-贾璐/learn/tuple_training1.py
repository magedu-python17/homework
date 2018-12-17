#!/usr/bin/env python


from collections import namedtuple

point = namedtuple("Key",["x","y"])
p1 = point(1,2)
print(p1.x,p1.y)
