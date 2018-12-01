
def add_zeo(b_s,n):
    if len(b_s) == n:
        for _ in range(8-n):
            b_s += '0'
    return b_s

s = '10.3.9.12'
l_s = s.split('.')
print(l_s)
for x in l_s:
    tmp = int(x)
    b_s = ''
    while True:
        if tmp == 0:
            break
        b_s += str(tmp % 2)
        tmp //= 2
    for n in range(1,8):
        b_s = add_zeo(b_s, n)
    print('{:<2} {:>8}'.format(x,b_s[::-1]))


# 10//2 = 5 0
# 5//2 = 2 1
# 2//2 = 1 0
# 1//2 = 0 1