#*******************************************
#     My blog:http://www.my-blog.top       #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************

triangle = []
n = int(input('num:'))
for i in range(n): #用循环将整个列表需要的内存空间事先整理出来
    row = [1]*(i+1)
    triangle.append(row) #将内存地址传给triangle
    for j in range(1,i//2+1): #每一行最多需要算几次，因为是对折，所以最多只要算行数的一半，j从1开始，所以后面要加1
        val = triangle[i-1][j-1]+triangle[i-1][j] #上一行的第j-1个元素加上上一行的第j个元素，并赋值给val
        row[j]=val #再将val填入当前行的第j个元素
        if i !=2*j: #这里是关键，可以理解为，只要不满足i==2*j这个条件就将值对折
            row[-j-1]=val
    print(triangle[i]) #打印二维列表的第i个元素就是打印当前行
