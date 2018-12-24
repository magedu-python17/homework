#*******************************************
#     my blog : http://101.132.77.52       #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
#输入奇数打印菱形
a=int(input('num:'))
if a%2:
    for i in range(-a//2+1,a//2+1):
        if i>=0:
            print(' '*i,'*'*(a-i*2))
        else:
            print(' '*(-i),'*'*(a+i*2))
else:
    print('ERROR!Pls input a odd number!')
