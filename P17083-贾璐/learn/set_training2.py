#!/usr/bin/env python

name = input("Enter a name: ")

A = {"B","C","D"}
B = {"A","C"}
C = {"A","B"}
D = {"A"}
total = A | B | C | D 

if name not in total:
    print("{}与群里其他人都不是微信朋友关系".format(name))

