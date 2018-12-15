#!/usr/bin/env python

count2 = 1
count3 = 5
print(7*"*")
for i in range(3,8,2):
    print(count2*" "+count3*"*"+count2*" ")
    count2 += 1
    count3 -= 2
for i in range(3,8,2):
    count1 = int((7-i)/2)
    print(count1*" "+i*"*"+count1*" ")
        
