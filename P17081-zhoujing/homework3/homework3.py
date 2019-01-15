def fun(string):
	return ''.join(sorted(string,key=lambda c:(c.isdigit(), c.isdigit() and int(c)%2==1, c.isupper())))

s='Sorting1234'
print(fun(sorted(s)))
