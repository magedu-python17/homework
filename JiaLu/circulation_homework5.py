#!/usr/bin/env python
count = 0
for num in range(100000):
    if num ==0 or num == 1:
        continue
    elif num == 2 or num == 3:
        print(num,end=" ")
        count += 1
    else: 
        if num % 2 == 0:
            continue
        else:
            for i in range(3,num):
                if num % i == 0:
                    break
            else:
                print(num,end=" ")
                count += 1
print("\n")
print("%d\n" % count) 
