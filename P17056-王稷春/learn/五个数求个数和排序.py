#!/usr/bin/python
n=[]
for i in range(5):
    n.append(int(input('{}:'.format(i))))
print(len(str(n[0])))
print(len(str(n[1])))
print(len(str(n[2])))
print(len(str(n[3])))
print(len(str(n[4])))
n.sort()
print(n)
