#!/usr/bin/python
n=int(input("请输入您想输入的数字个数:"))
a=[]
for i in range(n):
    a.append(int(input(f"请输入第{i}个数:")))
for j in range(n):
    print(f"您输入的第{j}个数值的个数是{len(str(a[j]))}位数")
q=len(a)
for x in range(q):
    for y in range(q-x-1):
        if a[y]>a[y+1]:
            a[y],a[y+1]=a[y+1],a[y]
print(a)

