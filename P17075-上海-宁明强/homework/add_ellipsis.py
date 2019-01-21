def add_elipsis(lst,elnum=4):
    for i in lst:
        print('{}{}'.format(i[:elnum],'...'))
comments = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)
add_elipsis(comments,elnum=6)
