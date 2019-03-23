def add_elipsis(lst,elnum=4):
    for i in lst:
        print('{}{}'.format(i[:elnum],'...'))
comments = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)
add_elipsis(comments,elnum=6)

# 这样写，逻辑上也能行，对了 区分下目录哈