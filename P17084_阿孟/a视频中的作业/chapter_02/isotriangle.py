#*******************************************
# Welcome to My blog http://www.my-blog.top
#*******************************************

#print square
s=int(input("num:"))
for y in range(s):  #Count.Record how many times you enter.
	for x in range(s):
		if y==2*x-s+1 or y==-2*x+s-1 or y==s-1:
			print("*",end='')
		else:
			print(" ",end="")
	print()
