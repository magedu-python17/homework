#!/usr/bin/env python

for num in range(100000):
    if num <= 3:
        print(num,end=" ")
    else: 
        if num % 2 == 0:
            continue
        else:
            for i in range(3,num):
                if num % i == 0:
                    break
            else:
                print(num,end=" ")
print("\n")
        
        
