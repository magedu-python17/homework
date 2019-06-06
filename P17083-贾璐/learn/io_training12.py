#!/usr/bin/env python

from os import path

p = path.join("/etc","sysconfig","network")
print(p)
print(type(p))
print(path.exists(p))
print(path.split(p))
print(path.abspath("."))
print(path.abspath(__file__))
print(path.basename(p))
print(path.dirname(p))
print(path.splitdrive(p))
