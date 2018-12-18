#!/usr/bin/env python

nums = input("Enter five numbers(num1 num2 num3 num4 num5): ")
stringlist = nums.split(" ")
numlist = []
for i in stringlist:
    numlist.append(int(i))
numlist.sort()
for i in range(len(numlist)):
    print("{:<15} : {:<3} bit".format(numlist[i],len(str(numlist[i]))))
