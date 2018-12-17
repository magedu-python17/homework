#!/usr/bin/env python

line = int(input("Enter a number: "))
line1 = line // 2
line2 = line - line1
for i in range(line+1):
    if i < line2:
        print(" "*i + "*"*(line-i*2))
    elif i == line2:
        continue
    else:
        print(" "*(line-i) + "*"*(line-(line-i)*2))
       
