#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-15 16:59
#
# Filename: homework_week04.py
#
# Description: V1.0
#
#========================================================
#
comments = (
    "Implementation note",
    "Changed",
    "ABC for generator",
    "Hello python"
)

def add_ellipsis(n,word):
    for i in word:
        lst = []
        for j in i:
           lst.append(j)
        print('{}{}'.format(''.join(lst[:n]),'......'))
#test:
add_ellipsis(5,comments)
