#!/usr/bin/env python

line = int(input("Enter a number: "))

for i in range(-line//2,line//2+1):
    if i < 0:
        print(" "*(-i)+"*"*(line+2*i))
    else:
        print(" "*i+"*"*(line-2*i))
