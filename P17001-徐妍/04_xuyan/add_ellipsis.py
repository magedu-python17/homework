#有一个列表，里面装着很多用户评论，为了在页面正常展示，
#需要将所有超过一定长度的评论用省略号替代
#我们拿到的评论不再是被继续装在列表里，而是在不可变的元组里呢？
comments = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]
comments2 = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]
'''
def add_ellipsis(set_len,iterable):
    lst=[]
    for item in iterable:
        if len(item) >set_len:
            lst.append(item[0:set_len]+'...')
        else:
            lst.append(item)
    return lst
'''
def add_ellipsis(set_len,iterable):
    return([item[:set_len]+'...' if len(item) > set_len else item for item in iterable])

print('\n'.join(add_ellipsis(11,comments)))
print('-------------')
print('\n'.join(add_ellipsis(5,comments2)))

# 没有问题~