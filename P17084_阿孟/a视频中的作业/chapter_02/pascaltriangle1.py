#*******************************************
#     my blog : http://www.my-blog.top     #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
triangle = [[1],[1,1]] #列出最开始的两特殊项
n=8
for i in range(2,n): #计数，产生大列表的新元素（杨辉三角的新行）
    newline = [1] #新行的首项
    pre = triangle[i-1] #将杨辉三角列表中的当前最后一个元素抽出，为计算下一元素做准备
    for j in range(i-1): #从0开始计数
        val = pre[j]+pre[j+1] #将抽出的元素从当前项开始累加
        newline.append(val) #累加的值循环堆入下一行
    newline.append(1) #最后堆入最后一项1
    triangle.append(newline) #将新生成的元素再堆入杨辉三角列表
print(triangle)
