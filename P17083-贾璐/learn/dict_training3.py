#!/usr/bin/env python
import random
strs = "abcdefghijklmnopqrstuvwxyz"
d = {}
count = 100
new_str = ""
while count > 0:
    for i in range(2):
        index = random.randint(0,len(strs)-1)
        new_str += strs[index]
    if new_str not in d:
        d[new_str] = 1
    else:
        d[new_str] += 1
    count -= 1
    new_str = ""


lst = list(d.keys())
lst.sort(reverse=True)
for key in lst:
    print("{}:{}".format(key,d[key]))
