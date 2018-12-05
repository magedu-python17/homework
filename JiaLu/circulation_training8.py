#!/usr/bin/env python

nums = input("Enter two numbers: (num1 num2)")

num1 = int(nums.split(" ")[0])
num2 = int(nums.split(" ")[1])

if num1 > num2:
    print("%d %d" % (num1,num2))
elif num1 < num2:
    print("%d %d" % (num2,num1))
else:
    print("num1 equal num2!")
