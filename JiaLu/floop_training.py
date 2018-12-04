#!/usr/bin/env python

num = input("Enter a number(number < 100000): ")

count = len(num)

num = int(num)
if num > 100000:
    print("Please enter a number < 100000")
else:
    for i in range(count):
       # if i != 0:
        if num % 10 != 0:
            print(num % 10)
            num = num // 10
        else:
            print(num)

    print("This number's length is %d !" % count)
