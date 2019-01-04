#*******************************************
#     My blog:http://www.my-blog.top       #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************

n = int(input('num:'))
#n = 6
lst = [1]
print(lst)
#lst.insert(0,0)
#lst.append(0)
for i in range(1,n):
    new = [1]*(i+1)
    for j in range(1,i//2+1):
        new[j]=lst[j-1]+lst[j]
        if i!=2*j:
            new[-j-1] = lst[j-1]+lst[j]
    print(new)
    lst = new.copy()
    #lst.insert(0, 0)
    #lst.append(0)
    new.clear()
