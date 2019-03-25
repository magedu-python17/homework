#!/usr/bin/env python


def foo1(num,list1=[]):
    list1.append(num % 10)
    num = int(num / 10)
    return list1 if num == 0 else foo1(num,list1)


num = int(input("Enter a number:"))
print(foo1(num))

