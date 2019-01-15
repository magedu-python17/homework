"""
__author__ = 'Administrator'
__mtime__ = '2019/1/15'
# code is far away from bugs with the god animal protecting，I love animals.         
"""

comments = [
    "Implementain note",
    "Changed",
    "ABC for generator"
]
# comments = ( "Implementain note",
#     "Changed",
#     "ABC for generator"
#              )
# 第一版:我们接到用户的一个需求，有一个列表，里面有很多用户评论，为了在页面上正常显示，需要将所有超过一定长度的评论用省略号代替
# 第二版:我们接到用户的一个需求，有一个列表，里面有很多用户评论，为了在页面上正常显示，需要将所有超过一定长度的评论用省略号代替，如果有一天，我们拿到的评论不再是在
# 继续装在列表中，而是装在列表中

# 定义一个函数，专门用于截取字符串
def turn_str(sr,nu):
    """
    :param sr:接收传入的字符串
    :param nu: 整数类型，需要截取多少位字符串
    :return:返回截取好的字符串
    """
    s1 = ''
    ls1 = []
    ls2 = []
    ls1 = list(sr)
    if len(sr) < nu:
        for i in ls1:
            s1 = s1 + i
    else:
        for i in ls1[0:nu-3]:
            s1 = s1 + i
        s1 = s1 +'...'
    return s1

def add_ellipsis(ls,num1):
    """
    :param ls: 传入参数的类型，目前可接受列表和元祖
    :param num1:整数类型，需要截取的位数
    :return:返回是否截取后的结果
    """
    ls1 = []
    for i in ls:
        if len(i)>10:
            sr = turn_str(i,num1)
            ls1.append(sr)
        else:
            ls1.append(i)
    if type(ls)==tuple:
        ls2 = tuple(ls1)
        print(ls2)
    if type(ls) == list:
        print(ls1)

add_ellipsis(comments,14)