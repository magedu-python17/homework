#!/usr/bin/env python

num = int(input("Enter a number for square's length: "))

for i in range(num):
    i += 1
    if i == 1:
        print("* " * num)
    elif i < num:
        print("*" + " "*(2*num-3) + "*")
    else:
        print("* " * num)



