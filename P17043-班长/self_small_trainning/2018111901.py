#打印边长为n的正方形
n = int(input('input * num: '))
if n == 1:
    print('*')
if n == 2:
    print('*'*2+'\n'+'*'*2)
if n >= 3:
    print( '*' * n )
    for _ in range(n-2):
        print('*' + ' ' * (n-2)  + '*')
    print('*' * n)

#100以内所有奇数之和
sum = 0
for x in range(1,101,2):
    sum += x
print(sum)
