#!/usr/bin/env python

num = input("Enter a number(number < 100000): ")

count = len(num)

if count > 5:
    print("Please enter a number < 100000")
else:
    for i in num:
        print(i)

    print("This number's length is %d !" % count)
