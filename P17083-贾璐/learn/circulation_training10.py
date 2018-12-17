#!/usr/bin/env python

sum = 0
flag = True
num_list = []
while flag:
    num = float(input("Enter number: "))
    num_list.append(num)
    sum += num
    result = sum / len(num_list)
    print(result)
    op = input("Continue?(Y/N)")
    if op not in ["y","Y"]:
        flag = False
