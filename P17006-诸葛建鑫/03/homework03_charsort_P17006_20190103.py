#! /usr/bin/env python
# Author 'zhuge'
# date: 2019/1/3 15:35
# file: 03_char_sort.py
"""
    如：s = "Sorting1234" ，给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
    1 所有的小写字母在大写字母前面
    2 所有的字母在数字前面
    3 所有的奇数在偶数前面
"""
# 若c为小写字母, 构造为(False, False, False)
# 若c为大写字母，构造为(False, False, True)
# 若c为奇数，构造为(True, False, False)
# 若c为偶数，构造为(True, True, False)


def char_sort(s:str):
    return sorted(s, key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper()))


while True:
    get = input('<字符串> >>> ')
    print(char_sort(get.strip(', :')))

