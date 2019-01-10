#!/usr/bin/env python

import math

def yang(m):
    N = [1]
    count = 0
    while count < m:
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
        count += 1
    return N

def value_compute(m,k):
    M = math.factorial(m)
    K = math.factorial(k-1)
    P = math.factorial(m-k+1)
    N = int(M/(K*P))
    return N
m = int(input("输入你选择的行："))
k = int(input("输入你选择的元素序号："))
N = yang(m)
value = value_compute(m,k)
print(N)
print(value)
