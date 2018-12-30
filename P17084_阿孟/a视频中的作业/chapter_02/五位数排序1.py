#从最高位开始排序
x=input('pls input num:')
s=len(x)
y=int(x)
for i in range(s-1,-1,-1):
	u = y
	w = u//10**i
	print(w)
	y = y%10**i
	i+=1
