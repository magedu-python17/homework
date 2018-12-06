#!/usr/bin/env python

for i in range(1,10):
    s = ""
    for j in range(i,10):
        s += "{} * {} = {:<{}}".format(i,j,i*j,2 if j < 4 else 3)
    print("{:>100}".format(s))
