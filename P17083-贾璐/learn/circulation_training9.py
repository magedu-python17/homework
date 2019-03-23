#!/usr/bin/env python

nums = input("Enter some numbers: (num1 num2 ... numN)")

num_list = nums.split(" ")

max_num = int(num_list[0])
min_num = int(num_list[0])
for i in range(len(num_list)):
    if int(num_list[i]) > max_num:
        max_num = int(num_list[i])

print(max_num)
