#!/usr/bin/env python

line = int(input("Enter a number: "))

line1 = -(line//2)
line2 = line - line1
count = 1
for i in range(line1,line2):
    print(" "*abs(i)+"*"*(line-2*abs(i)))
    count += 1
    if count > line:
        break
