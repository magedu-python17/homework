def foo1(b, b1=3):
    print("foo1 called", b, b1)
def foo2(c):
    foo3(c)
    print("foo2 called", c)
def foo3(d):
    print("foo3 called", d)
def main():
    print("main called")
    foo1(100, 101)
    foo2(200)
    print("main ending")
main()