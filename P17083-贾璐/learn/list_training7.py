#!/usr/bin/env python

nums = input(">>> ")
num1 = int(nums.split(" ")[0])
num2 = int(nums.split(" ")[1])
num3 = int(nums.split(" ")[2])

max_num = max(num1,num2,num3)
min_num = 0
mid_num = 0
if num1 == max_num:
    if num2 > num3:
        mid_num = num2
        min_num = num3
    else:
        mid_num = num3
        min_num = num2
elif num2 == max_num:
    if num1 > num3:
        mid_num = num1
        min_num = num3
    else:
        mid_num = num3
        min_num = num1
else:
    if num1 > num2:
        mid_num = num1
        min_num = num2
    else:
        mid_num = num2
        min_num = num1


print("{} {} {}".format(max_num,mid_num,min_num))
    
