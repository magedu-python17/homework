#!/usr/bin/env python

num = int(input("Enter a number:"))
pre = 0
cur = 1
print(cur,end = ' ')

def foo1(n,pre=0,cur=1):
    pre,cur = cur,pre + cur
    print(cur,end = ' ')
    if n == 2:
        return
    else:
        foo1(n-1,pre,cur)
foo1(num)
print()
