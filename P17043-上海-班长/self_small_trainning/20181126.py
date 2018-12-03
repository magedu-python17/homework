#打印向右对齐。上三角的99乘法表
# for i in range(1,10):
#     s = ''
#     for j in range(i,10):
#         s += '{}*{} = {:<4}'.format(i,j,j*i)
#     print('{:>90}'.format(s))

#打印菱形
# line = 6
# if line % 2 == 0:
#     line += 1
# for x in range(-((line-1)//2),((line-1)//2+1)):
#     print('{}{}'.format(' '*abs(x),'*'*(line - abs(x)*2)))

# l   *  ' '
# 1   7   0
# 2   5   1
# 3   3   2
# 4   1   3
# 5   3   2
# 6   5   1
# 7   7   0

#打印倒三角
# line = 6
# if line % 2 == 0:
#     line += 1
# for i in range(-line,line+1,2):
#     if i == -1:
#         continue
#     print('{}{}'.format(' '*((line-abs(i))//2),'*'*abs(i)))
#
# print(0 and 2 or 1 or 4)

#打印闪电
# l '' *
# 1  3 1
# 2  2 2
# 3  1 3
# 4  0 6
# 5  3 3
# 6  3 2
# 7  3 1

line = 15
for x in range(-(line-1)//2,(line-1)//2):
    if x < 0:
        print('{}{}'.format(' '*(-x),'*'*((line-1)//2+x)))
    elif x == 0:
        print('*'*(line-1))
    elif x > 0:
        print('{}{}'.format(' '*((line-1)//2),'*'*((line-1)//2-x)))


#求斐波那契数列
# def fib():
#     a,b = 0,1
#     count = 0
#     while count < 100:
#         yield b
#         a , b = b , a + b
#         count += 1
# g = fib()
# for _ in range(100):
#     print(next(g))

#求10万以内质数
# import  time
# start = time.time()
# count = 0
# for jj in range(3,100000,2):
#     if jj > 10 and jj % 10 == 5:
#         continue
#     for ii in range(3,int(jj**(0.5))+1):
#         if jj % ii == 0:
#             break
#     else:
#         #print(jj)
#         count += 1
# print(count)
# print(time.time()-start)
