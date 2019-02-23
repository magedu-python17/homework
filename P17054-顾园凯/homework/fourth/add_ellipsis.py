#定义函数
def add_ellipsis(comment):
    lst = []
    for i in range(len(comment)):
        if len(str(comment[i])) >= 10:
            lst.append(str(comment[i])[:10]+'...')
        else:
            lst.append(str(comment[i]))
        print(lst[i])
    if type(comment) == tuple:
        return tuple(lst)
    else:
        return lst
add_ellipsis((
    "Implementation note",
    "Changed",
    "ABC for generator"
))