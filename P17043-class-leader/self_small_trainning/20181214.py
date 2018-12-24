#冒泡排序算法

a = [1,22,43,3,12,65,23,0,-1,-100]
for i in range(len(a)):
    flag = True
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            flag = False
    if flag:
        break
print(a)


for i in range(2):
    print(i)
else:
    print('complete 1')

# for i in range(2):
#     print(i)
# else:
#     print('complete 2')