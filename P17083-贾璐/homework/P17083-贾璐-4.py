#!/usr/bin/env python

def add_ellipsis(input_type,comments):
    if input_type == list:
        for i in comments:
            if type(i) != str:
                i = str(i)
            if len(i) > 7:
                print(i[:7] + "...")
            else:
                print(i)
    elif input_type == tuple:
        for i in comments:
            if type(i) != str:
                i = str(i)
            if len(i) > 7:
                print(i[:7] + "...")
            else:
                print(i)
    else:
        print("wrong input type!")



comments = ("Implementation note",
            "Changed",
            "ABC for generator")

input_type = type(comments)

add_ellipsis(input_type,comments)
