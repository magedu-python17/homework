#!/usr/bin/env python


num = input(">>> ")

num1 = int(num.split(" ")[0])
num2 = int(num.split(" ")[1])
num3 = int(num.split(" ")[2])

max_num = num1
min_num = num1
mid_num = num1

if num2 < min_num:
    if num3 < num2:
        min_num = num3
    else:
        min_num = num2
        mid_num = num3
elif num3 < min_num:
    min_num = num3
    max_num = num2
elif num2 > num3:
    max_num = num2
    mid_num = num3
else:
    max_num = num3
    mid_num = num2

print("%d %d %d" % (max_num,mid_num,min_num))
