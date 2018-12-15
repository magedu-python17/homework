#!/usr/bin/env python

for i in range(1,10):
    for j in range(1,i+1):
        if i == j:
            print("%d * %d = %d" % (j,i,j*i))
        else:
            print("%d * %d = %d" % (j,i,i*j),end="\t")
    print()
