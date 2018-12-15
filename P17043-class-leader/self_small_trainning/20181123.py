#三种求 5！+ 4！+ 3！+ 2！+ 1！之和的方法

def cross(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
sum = 0
for i in range(1,6):
    sum += cross(i)
print(sum)


sum = 0
a = 1
for i in range(1, 6):
    a *= i
    sum += a
print(sum)

print(cross(6))


def cross(n):
    if n == 1:
        return 1
    if n >= 1:
        return n * cross(n-1)
sum = 0
for i in range(1,6):
    sum += cross(i)
print(sum)

