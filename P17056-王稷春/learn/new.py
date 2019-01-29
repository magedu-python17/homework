#!/usr/bin/python
n=int(input("请输入您想输入的数字个数:"))
a=[]
for i in range(n):
    a.append(int(input(f"请输入第{i}个数:")))
for j in range(n):
    print(f"您输入的第{j}个数值的个数是{len(str(a[j]))}位数")
a.sort()
print(a)

