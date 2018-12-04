#!/usr/bin/env python

total_sum = 0
factorial = 1
for i in range(5):
    i += 1
    for j in range(i):
        j += 1
        factorial *= j
    total_sum += factorial
    factorial = 1

print(total_sum)
