#!/usr/bin/env python
from copy import deepcopy
def test(n):
    N = [1]
    count = 0
    while count < n:
        print(N)
        N.append(0)
        if len(N) % 2 == 0:
            N = [N[i-1] + N[i] for i in range(int(len(N)/2))]
            M = deepcopy(N)
            M.reverse()
            N += M
        else:
            mid = [N[int((len(N)/2)-1)] + N[int(len(N)/2)]]
            N = [N[i-1] + N[i] for i in range(int(len(N)/2))]
            M = deepcopy(N)
            N = N + mid + M
        count += 1


count = int(input(">>> "))
test(count)
