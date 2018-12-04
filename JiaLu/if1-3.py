#!/usr/bin/env python

def check_num(num):
    count = len(num)
    if count < 6:
        print(count)
    elif count == 0 or count > 6:
        print("Wrong number!")

a = input("Enter a number: (MAX 99999)")

check_num(a)
