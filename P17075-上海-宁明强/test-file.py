def foo(xyz=[], u='abc', z=123):
    xyz.append(1)
    def inner(a=10):
        pass
    print(inner)
    def inner(a=100):
        print(xyz)
    print(inner)
    return inner
bar = foo()
#print(id(foo),id(bar), foo.__defaults__, bar.__defaults__)
del bar
#print(id(foo),id(bar), foo.__defaults__, bar.__defaults__)