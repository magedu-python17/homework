#!/usr/bin/env python


line = int(input("Enter a number: "))

line1 = line // 2

for i in range(-line1,line-line1):
    count = -i if i < 0 else i
    print(" "*(line1-count)+"*"*(2*count+1))
