#*******************************************
#     my blog : http://101.132.77.52       #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
#
s=int(input('odd num:'))
if s%2:
	for i in range(-s//2,s//2+1):
		if i<0:
			print(' '*(-i-1),((s//2+1)+i)*'*')
		elif i==0:
			print(s*'*')
		else:
			print((s//2-1)*' ',((s//2+1)-i)*'*')
else:
	print('ERROR!Pls input odd number!')
