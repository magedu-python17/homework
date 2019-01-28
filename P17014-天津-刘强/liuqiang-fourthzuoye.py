comments = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]
def func(comments,max = 6):
    lst = []
    for string  in  comments:
        if len(string) > max:
            lst.append(string[:max] + '...')
        else:
            lst.append(string)
    return  lst
print("\n".join(func(comments)))


def add(comments, max_length):
    for comment in comments:
        comment = comment.strip()
        if len(comment) > max_length:
            yield comment[:max_length] + '...'
        else:
            yield comment
comments = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)
x = add(comments,7)
for i in x:
    print(i)

# 不错。第二种更通用一些