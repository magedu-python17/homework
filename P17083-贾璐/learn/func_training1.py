#!/usr/bin/env python

def diff_nums(*args):
    min_num = min(args)
    max_num = max(args)
    return (min_num,max_num)

nums = input("Enter two number: ").split(" ")

min_num,max_num = diff_nums(*nums)

print(min_num,max_num)
