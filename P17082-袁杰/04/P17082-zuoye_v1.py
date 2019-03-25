#comments = [
#    "Implementation note",
#    "Changed",
#    "ABC for generator",
#]
#第一版：我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代,请写出 一个add_ellipsis 函数方法来实现
#第二版:我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代，如果有一天，我们拿到的评论不再是被继续装在列表里，而是在不可变的元组里呢？
#请写出 一个add_ellipsis 函数方法来实现

comments_1 = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]

comments_2 = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)


def add_ellipsis_1(n,comments):
    for i in comments:
        if len(i) > n:
            print(i[:n] + '...')
        else:
            print(i)
add_ellipsis_1(10,comments_1)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
add_ellipsis_1(7,comments_2)
