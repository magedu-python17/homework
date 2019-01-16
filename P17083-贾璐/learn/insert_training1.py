#!/usr/bin/env python

def insert_list(*args):
    lst = [int(x) for x in args]
    new_lst = [0] + lst
    length = len(new_lst)
    for i in range(2,length):
        new_lst[0] = new_lst[i]
        j = i - 1
        if new_lst[j] > new_lst[0]:
            while new_lst[j] > new_lst[0]:
                new_lst[j+1] = new_lst[j]
                j -= 1
            new_lst[j+1] = new_lst[0]
    return new_lst[1:]


numbers = input("Enter numbers: ")

lst = numbers.split(" ")

print(insert_list(*lst))
