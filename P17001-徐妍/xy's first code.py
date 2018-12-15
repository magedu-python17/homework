#5个数字排序 #冒泡法的标记
n=int(input('>>>how many?>>>'))
lst=[]
for x in range(n):
    m=int(input('>>>>'))
    lst.append(m)
swap=0
for i in range(n-1):
    flag=False
    for j in range(n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            flag=True
            swap+=1
    if not flag:
        break
print(lst)
print(swap)








