import re
comments = ['lmplementation note', 'changed', 'ABC for generator']
pattern = "......"


def add_ellipsis(n: int, string):
    for i in range(len(string)):
        if len(string[i]) >= n:
            regex = re.compile(string[i][n:])
            newstr = regex.sub(pattern, string[i])
            string[i] = newstr

    print(string)


add_ellipsis(10, comments)

# 元组的话是不是可以转成列表后操作，不知道理解的对不对
# comments = ('lmplementation note', 'changed', 'ABC for generator')
# pattern = "......"
#
#
# def add_ellipsis(n: int, string):
#     comment = list(string)
#     for i in range(len(comment)):
#         if len(comment[i]) >= n:
#             regex = re.compile(comment[i][n:])
#             newstr = regex.sub(pattern, comment[i])
#             comment[i] = newstr
#     print(comment)

#
# add_ellipsis(4, comments)