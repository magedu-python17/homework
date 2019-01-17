#!/usr/bin/python
n=0
x=int(input("多少以内的:"))
for i in range(x+1):
    if i%2>0:
        n+=i
    else:
        continue
    print(n)
