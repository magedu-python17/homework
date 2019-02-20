#
# def counter(base):
#     def inc(step=1):
#         nonlocal base
#         base += step
#         return base
#     return inc
#
# c1 = counter(10)
# c2 = counter(10)
#
# print(c1 == c2)
# print(c1 is c2)
#

#高阶函数
def sort(iterable,reverse=True,key=lambda x,y: x<y):
    ret = []
    for x in iterable:
        for i,v in enumerate(ret):
            flag = key(x,v) if not reverse else not key(x,v)
            if flag:
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sort([11,2,34,10,24,26]))

