#从最低位开始排序
x=input('pls input num:')
s=len(x)
y=int(x)
for i in range(s):
	u = y
	w = u%10
	print(w)
	y = y//10
