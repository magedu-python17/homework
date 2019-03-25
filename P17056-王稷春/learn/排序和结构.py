#!/usr/bin/python
n=[9,8,1,5,6,3,2,0]
a=len(n)
for i in range(a):
    for k in range(a-1-i):
        if n[k]>n[k+1]:
            n[k],n[k+1]=n[k+1],n[k]
print(n)



key,_,val="JAVA_HOME=/usr/bin".partition('=')
print(key)
print(val)
