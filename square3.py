#*******************************************
# welcome to my blog : http://101.132.77.52
#*******************************************

#print square
s=int(input("num:"))
for y in range(s):  #Count.Record how many times you enter.
    for x in range(s):
        if x==0 or y==0 or y==s-1 or x==s-1: #x为横坐标，y为纵坐标，打印直线并平移,这里要注意range(s)的包左不包右的特性
            print("*",end='')
        else:
            print(" ",end="")
    print()
