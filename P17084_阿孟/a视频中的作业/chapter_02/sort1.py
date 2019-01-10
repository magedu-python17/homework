#*******************************************
#     my blog : http://www.my-blog.top     #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
#
num = []
n = int(input('How many num do u want sort?   '))
print('num:')
for t in range(n):
    num.append(int(input()))
lenth = len(num)
for i in range(lenth-1):
    for j in range(lenth-1):
        if num[j]>num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]
print(num)
