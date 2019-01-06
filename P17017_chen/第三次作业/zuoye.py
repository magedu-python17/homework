def fun(string):
    a = []
    b = []
    c = []
    d = []
    for x in string:
        if x.isalpha() and x.islower():
            a.append(x)
        elif x.isupper():
            b.append(x)
        if x.isdigit() and int(x) % 2 == 0:
            d.append(x)
        elif x.isdigit():
            c.append(x)
    newstring = ''.join(sorted(a) + sorted(b) + sorted(c) + sorted(d))
    return newstring


new_string = input('请输入字符串：')
print(fun(new_string))

# 想想 fun 里面的是不是可以用几行代码来代替呢？