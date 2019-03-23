#coding=utf-8
#练习:依次接收用户输入3个数,排序后打印
#1.转换int后,判断大小排序,使用分支结构完成
a=int(input("请输入第一个数:"))
b=int(input("请输入第二个数:"))
c=int(input("请输入第三个数:"))
if a<=b:
    if a<=c:
        if b<=c:
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        print(b,a,c)
else:
    if b>=c:
        print(a,b,c)
    else:
        if a>=c:
            print(a,c,b)
        else:
            print(c,a,b)


#coding=utf-8
a=int(input("first number:"))
b=int(input("second number:"))
c=int(input("thied number:"))
if a>=b:
    if a>=c:
        if b>=c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if c>=b:
        print(c,b,a)
    else:
        if c>=a:
            print(b,c,a)
        else:
            print(b,a,c)
