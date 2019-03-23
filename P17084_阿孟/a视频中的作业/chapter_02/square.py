#*******************************************
# Welcome to My blog http://www.my-blog.top
#*******************************************

#print square
s=int(input("num:"))
for i in range(s):  #Count.Record how many times you enter.
    if i == 0 or i == s-1:  #If i is 0 or you enter minus 1,print '*' in all line and without wrap
        for i in range(s):
            print('*',end='')
        print('')
    else:
        print('*',end='')   #先打印第一个*
        for i in range(s-2):    #循环打印空格
            print(' ',end='')
        print('*')  #打印最后的*

