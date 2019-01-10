#!/usr/bin/env python

def str_sort(string):    #字符排序函数
    tmp = []
    for x in string:
        tmp.append((x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(),x))    #添加元组，数组格式：(是否是数字,是否是偶数,是否是大写,是否是小写,字符本身)   这个顺序是根据题目要求来决定的！
    new_string = ''.join(map(lambda x:x[-1],sorted(tmp)))     #先将tmp里面的元素----元组进行排序，然后通过map函数进行取每一个元组的最后一个元素并通过join方法组合成新的字符串并赋值给new_string变量
    return new_string     #返回这个新字符串


string = input("Please Enter a string: ")

new_string = str_sort(string)

print(new_string)


# 试试再简洁一些，代码还可以优化