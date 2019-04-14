#!/usr/bin/env python

d = {}

enter = int(input(">>>"))
while True:
    if enter // 10 != 0:
        num_key = enter % 10
        enter = enter // 10
        if num_key in d.keys():
            d[num_key] += 1
        else:
            d[num_key] = 1
    else:
        num_key = enter
        if num_key in d.keys():
            d[num_key] += 1
        else:
            d[num_key] = 1
        break

print(d)
