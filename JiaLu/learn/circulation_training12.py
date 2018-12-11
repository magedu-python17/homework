#!/usr/bin/env python
count = 1
count2 = 16
for i in range(1,10):
    for j in range(count,10):
        if i == 1:
            print("%d * %d = %d" % (i,j,i*j),end="\t")
        else: 
            if i == j:
                print(" "*count2*(i-1),end="")
            print("{} * {} = {}".format(i,j,i*j),end="\t")
        if count != 10:
            count += 1
    count = i+1
    print()
