#! /usr/bin/env python
# Author 'zhuge'
# date: 2019/1/14 17:42
# file: 04_comment_process.py
comment = (
    "Implementation note",
    "Changed",
    "ABC for generator"
)


def add_ellipsis(length, iterable):
    return (item if len(item) < length else item[0:length]+'......' for item in iterable)


print('\n'.join(list(add_ellipsis(10, comment))))

# 没有问题