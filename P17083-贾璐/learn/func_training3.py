#!/usr/bin/env python


def foo1(n):
    return 1 if n < 2 else foo1(n-1) + foo1(n-2)

n = int(input("Enter a number: "))
for i in range(n):
    print(foo1(i),end = " ")
print()
