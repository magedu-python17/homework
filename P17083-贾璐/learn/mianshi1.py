#!/usr/bin/env python

a = [6,4,-3,5,-2,-1,0,1,-9]
start = 0
end = len(a)
for i in range(len(a)):
    if a[start] > 0:
        start += 1
    else:
        temp,a[start] = a[start],a[end - 1]
        a[end - 1] = temp
    if a[end - 1] < 0:
        end -= 1
print(a)
