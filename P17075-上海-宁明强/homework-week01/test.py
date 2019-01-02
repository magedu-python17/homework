#接受一个参数n,n为正整数，左右两种打印方式，要求数字对齐
def f3(x):
    print(x)
    weight=(10*len(str(x)) )*2+x
    print(weight)
    for i in range(1,x+1):
#        print('{:>{}}'.format(' '.join(str(j) for j in range(i,0,-1)),weight))
        print('{:>{}}'.format(' '.join(sorted((str(j) for j in range(1,x-i)),reverse=True,key=int)),weight))

f3(22)
