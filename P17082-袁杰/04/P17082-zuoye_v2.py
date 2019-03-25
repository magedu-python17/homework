#comments = [
#    "Implementation note",
#    "Changed",
#    "ABC for generator",
#]
#第一版：我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代,请写出 一个add_ellipsis 函数方法来实现
#第二版:我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代，如果有一天，我们拿到的评论不再是被继续装在列表里，而是在不可变的元组里呢？
#请写出 一个add_ellipsis 函数方法来实现


comments = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)


def add_ellipsis(comments, n=10):
    for i in comments:
        if len(i) > n:
            yield i[:n] + '...'
        else:
            yield i
    # return (i[:n] + '...' if len(i) > n else i for i in comments)


print('\n'.join(add_ellipsis(comments)))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\n'.join(add_ellipsis(comments, 7)))