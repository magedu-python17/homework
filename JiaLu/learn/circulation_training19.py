#!/usr/bin/env python

num = int(input("Enter a number: "))

init = 1
sum = 0 
for i in range(num):
    init,sum = sum,sum+init
print(sum)



