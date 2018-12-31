#*******************************************
#     my blog : http://101.132.77.52       #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
#求10万以内的素数
#import datetime
#start = datetime.datetime.now()
print(2)
for i in range(3,100000,2): #从3开始，跳过偶数
    for j in range(3,int(i**0.5+1),2): #任何奇数都不会被偶数整除，所以再排除掉j中的偶数
        if i%j == 0:
            break
    else:
        print(i)
#stop = datetime.datetime.now()
#print(stop-start)
