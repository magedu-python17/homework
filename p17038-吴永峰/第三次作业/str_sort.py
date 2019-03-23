
s = "Sorting12345678"
b = "".join(sorted(s,key=lambda x:(x.isdigit() and int(x)%2 == 0,x.isdigit(),x.isupper(),x.islower(),x)))
print(b)