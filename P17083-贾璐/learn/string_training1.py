#!/usr/bin/env python

num = input("Enter a number: ")

if num.isdecimal():
    print("This number is {} bit number!".format(len(num)))
    for i in range(len(num)):
        print("{} : {} counts!".format(num[i],num.count(num[i])))
else:
    print("Please enter a number!")

