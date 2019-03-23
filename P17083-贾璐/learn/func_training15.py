#!/usr/bin/env python

def max_str(str1,str2):
    return str1 if len(str1) >= len(str2) else max_str(str2,str2)


str1 = input("Enter str1:")
str2 = input("Enter str2:")

print(max_str(str1,str2))
