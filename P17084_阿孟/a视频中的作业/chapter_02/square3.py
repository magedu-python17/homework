#*******************************************
# Welcome to My blog http://www.my-blog.top
#*******************************************

#print square
s=int(input("num:"))
for y in range(s):  #Count.Record how many times you enter.
	for x in range(s):
		if y==0 or x==0 or y==s-1 or x==s-1: #类似于在二维坐标轴上用4条直线绘制出正方形
			print("*",end='')
		else:
			print(" ",end='')
	print()
