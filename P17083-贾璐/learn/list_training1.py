#!/usr/bin/env python

def test(n):
    N = [1]
    count = 0
    while count < n:
        print(N)
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
        count += 1


count = int(input(">>> "))
test(count)
