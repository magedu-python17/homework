

#数字判断
a=input('>>>')
print(len(a))
for i in range(1,len(a)+1): #从个位开始，打印其位数和出现次数
    print(a[-i],a.count(a[-i]))


import copy
a=[1]*5
for i in range(5):
    a[i]=int(input('请输入:'))
b=copy.deepcopy(a)
b.sort(key=int,reverse=False)
print(a)
print(sorted(a))
print(b)

