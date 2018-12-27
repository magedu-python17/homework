#*******************************************
# Welcome to My blog http://www.my-blog.top
#*******************************************
#
s=int(input('num:'))
if s!=1:
    for i in range(2,s):
        if s%i==0: #在遍历整个2-s时如果s满足了if的条件，则break整个for循环，不再执行for中的else
            print(s,'is not prime')
            break
    else: #遍历整个2-s后如果s没有满足上一条if语句s%i==0，则执行for语句中的else
        print(s,'is prime')
else:
    print(1,'is not prime')
