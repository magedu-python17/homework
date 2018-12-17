#!/usr/bin/env python

line = int(input("Enter a number: "))
line1 = line // 2
line2 = line - line1

for i in range(-line1,line2):
    if i < 0:
        count = -i
        count2 = line
    elif i == 0:
        count = i
        count2 = -(line2)
    else:
        count = line1
        count2 = line
    print(" "*count+"*"*abs(count2-(line1+abs(i))))
