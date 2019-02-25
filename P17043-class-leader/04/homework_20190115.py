# 本周大作业来袭，小伙伴要按时提交哦（1.14-1.27）
# 作业内容如下：
# 要求至少学到第18节课程
# comments = [
#     "Implementation note",
#     "Changed",
#     "ABC for generator",
# ]
# 第一版：我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代,请写出 一个add_ellipsis 函数方法来实现
# 第二版:我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代，如果有一天，我们拿到的评论不再是被继续装在列表里，而是在不可变的元组里呢？
# 请写出 一个add_ellipsis 函数方法来实现

comments = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]

def add_ellipsis(comments,length=5):
    return (x[0:length] + '...' if len(x) > length else x for x in comments)
    # for x in comments:
    #     if len(x) > length:
    #         yield x[0:length] + '...'
    #     else:
    #         yield x

gener = add_ellipsis(comments,length=4)

print('\n'.join(gener))

# 下次尽量提前交作业哈