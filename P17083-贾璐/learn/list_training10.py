#!/usr/bin/env python

def test(n):
    N = [1]
    count = 0
    while count < n:
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
        count += 1
    return N


mk = input(">>> ")
count = int(mk.split(' ')[0])
index = int(mk.split(' ')[1])
list1 = test(count)
print(list1[index - 1])
