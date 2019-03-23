#分解质因数

# num = 128
# a = num
# lst = []
# while num != 1:
#     for i in range(2,num+1):
#         if num % i == 0:
#             lst.append(i)
#             num //= i
#             break
#
# print(a,'=','*'.join(map(str,lst)))

#杨辉三角
def trangle():
    def aaa(i):
        new_ret = [1]
        for x in range(0, i - 2):
            new_ret.append(ret[i - 2][x] + ret[i - 2][x + 1])
        new_ret.append(1)
        ret.append(new_ret)
    ret = []
    n = int(input('请输入层数：'))
    tmp = [1]
    for i in range(1,n+1):
        if i < 3:
            ret.append(tmp * i)
        for j in range(3,n+1):
            if i == j:
                aaa(i)
                break
    for xxx in ret:
        print(xxx)

trangle()


# 如何判断一个字符串可以转换成整形数字？有啥好办法不？
a = '123456abvcsAAA'
res = map(lambda x:x.isdigit(),a)
print(list(res))
