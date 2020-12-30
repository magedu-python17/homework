def fun(string):
	return ''.join(sorted(string,key=lambda c:(c.isdigit(),c.isdigit() and int(c)%2==0,c.isupper())))

s='qwertyuiopasdfghjklzxcvbnmQWETUIOPASDFGHJKLZXCVBNM963852741'
print(fun(sorted(s)))
