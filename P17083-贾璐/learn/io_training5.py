#!/usr/bin/env python

file1_list = []
with open("/home/python/python_project/3.5.3/homework/P17083-贾璐/test/1","r") as f:
    for line in f.readlines():
        file1_list.append(line)

with open("/home/python/python_project/3.5.3/homework/P17083-贾璐/test/1.1","w+") as f:
    for line in file1_list:
        f.write(line)
    
