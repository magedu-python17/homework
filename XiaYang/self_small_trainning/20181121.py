# s = "MageduPython1234567" 我想要实现以下功能:
# 1 所有的小写字母在大写字母前面
# 2 所有的字母在数字前面
# 3 所有的奇数在偶数前面
#  有没有小伙伴用一行代码写出来的？

# s = "MagedyPython1234567"
#
# print(*sorted('MageduPython1234567',key=lambda a:(a.isdigit() - a.islower(),a in '02468',a)),sep='')
#
# tmp = "".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)))
# print(tmp)
#
#
# def aaa(x):
#     print(x.isdigit(),x.isupper())
#
#
# print(aaa('a'))

#打印一个边长为n的正方形
# n = 5
# e = -n//2
# for i in range(e,n+e):
#     if i == e or i == n+e-1:
#         print('*'*n)
#     else:
#         print('*'+' '*(n-2)+'*')

# #99乘法表
ret = ''
for x in range(1,10):
    for y in range(1,10):
        ret += '{}*{}={} '.format(y,x,y*x)
        if x == y:
            ret += '\r\n'
            break
print(ret)



#我现在想快速统计里面每个元素出现的个数，有什么方法实现吗？注意要快速
a = [1,1,2,3,4,5,6,8,8]
ret = {}
for x in a:
    if x not in ret:
        ret[x] = 1
    else:
        ret[x] += 1
print(ret)
