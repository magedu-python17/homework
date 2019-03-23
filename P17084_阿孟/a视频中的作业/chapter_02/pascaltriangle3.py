#*******************************************
#     my blog : http://www.my-blog.top     #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
n = int(input('num:'))
lst = [1]
print(lst)
lst.insert(0,0)
lst.append(0)
for i in range(1,n):
    new = []
    for j in range(i+1):
        new.append(lst[j]+lst[j+1])
    print(new)
    lst = new #将结果重新给lst准备下一次循环打印下一行
    lst.insert(0, 0)
    lst.append(0)
