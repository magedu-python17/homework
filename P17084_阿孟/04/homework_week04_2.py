#========================================================
#
# Author: AM readygood@163.com
#
# Blog: http://www.my-blog.top
#
# Last modified: 2019-01-15 17:57
#
# Filename: homework_week04_2.py
#
# Description: V1.0
#
#========================================================
#
#简化为列表解析式
n = int(input('How many string do you want to stay? >>> '))
comments = (
    "Implementation note",
    "Changed",
    "ABC for generator",
    "Hello python"
)
def add_ellipsis(n,word):
    for i in word:
        lst = [j for j in i] #简化为列表解析式
        print('{}{}'.format(''.join(lst[:n]),'......'))
#test:
add_ellipsis(n,comments)

# 想想生成器的写法