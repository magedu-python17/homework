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
n = 4
e = -n//2
for i in range(e,n+e):
    if i == e or i == n+e-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')


