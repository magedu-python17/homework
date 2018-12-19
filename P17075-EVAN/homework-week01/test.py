from operator import itemgetter, attrgetter
userInfo = [['zhangsan','18','13533333333'],['lishi','22','13733333333'],['wangwu','38','12344444444'],['zhaoliu','44','13788228888']]
b='wuage:33:454545'
bb=b.split(':')
bb
userInfo.extend([bb])
print(userInfo)
#userInfo[5]
print(sorted(userInfo,key=itemgetter(0)))
print(sorted(userInfo,key=itemgetter(1)))
print(sorted(userInfo,key=itemgetter(2)))

