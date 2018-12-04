#!/usr/bin/env python

num = input("Enter a number (number < 100000): ")

count = len(num)

num = int(num)

if num >= 100000:
    print("Please enter a number < 100000!")
else:
    print("This number's length is %d" % count)
    count -= 1
    while count >= 0:
        if num % (10 ** count) != 0:
            print(num // (10 ** count))
            num = num % (10 ** count)
            count -= 1
        else:
            count -= 1
            print(num)
