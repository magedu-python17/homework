#*******************************************
#     my blog : http://www.my-blog.top     #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************

n = 100000
lst = []
flag = True
print(2)
for i in range(3,n,2):
    up = i**0.5
    for j in lst:
        if j > up:
            flag = True
            break
        if i % j ==0:
            flag = False
            break
    if flag:
        print(i)
        lst.append(i)
