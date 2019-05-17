#!/usr/bin/env python



with open("test","w+") as f:
    f.writelines("123\n456\n789\n")

with open("test","r+") as f:
    for line in f.readlines():
        print(line.strip())



