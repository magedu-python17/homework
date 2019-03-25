def add(n,i):
    return n + i

def test():
    for i in range(4): yield i

g = test()
res = []

for n in [1,10,5]:
    g = (add(n,i) for i in g)

print(list(g))
print(list(add(5,i) for i in(add(10,1) for i in (add(1,i) for i in test()))))
