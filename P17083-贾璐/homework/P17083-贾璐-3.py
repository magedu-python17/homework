#!/usr/bin/env python

def str_sort(string):
    tmp = []
    for x in string:
        tmp.append((x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(),x))
    new_string = ''.join(map(lambda x:x[-1],sorted(tmp)))
    return new_string


string = input("Please Enter a string: ")

new_string = str_sort(string)

print(new_string)


