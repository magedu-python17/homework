#!/usr/bin/env python

lst = [1,4,9,16,2,5,10,15]

new_lst = [lst[i] + lst[i+1] for i in range(len(lst)-1)]

print(new_lst)
