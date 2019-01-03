#*******************************************
#     my blog : http://www.my-blog.top     #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
#
print([1]) #打印第0行
pre = [1,1] #打印第1行
print(pre)
n = 8
for i in range(2,n): #从第2行开始
    new = [1] #打印新行第一个元素
    line = pre #新建列表
    for j in range(i-1): #这里要注意边界，为什么是i-1？因为前一行的最大项索引是i-1
        new.append(line[j]+line[j+1]) #循环追加元素
    new.append(1) #追加最后一项
    print(new)
    pre = new #重新定义pre列表
