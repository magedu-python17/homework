a=[1,9,8,5,6,7,4,3,2]
for j in range(len(a)):
    for i in range(1,len(a)-j):
        if a[i-1]>a[i]:
            b=a[i-1]
            c=a[i]
            a[i-1]=c
            a[i]=b
        else:
            continue
print(a)