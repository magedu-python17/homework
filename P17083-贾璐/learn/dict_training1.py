#!/usr/bin/env python



d = {}
while True:
    enter = input(">>> ")
    if enter != "exit":
        num = int(enter)
    else:
        break
    if num in d.keys():
        d[num] += 1
    else:
        d[num] = 1
    print("{}:{}".format(num,d[num]))

