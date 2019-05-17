#!/usr/bin/env python
import re


def read_file(filename):
    list_file = []
    with open(filename) as f:
        for line in f.readlines():
            list_file.append(line.strip())
    return list_file


def check_word(list_name):
    new_list = []
    for i in list_name:
        new_i = re.sub(r"[-=\"\'`~©!@#$%^&*()_+/?<>,.\\/\[\]{}]|\r|\t"," ",i)
        if " " not in new_i:
            new_list.append(new_i)
        elif " " in new_i:
            new_i_list = new_i.split(" ")
            for new_i in new_i_list:
                new_list.append(new_i)
    return new_list


def word_count(filename):
    list_file = read_file(filename)
    strs_dict = {}
    for line in list_file:
        strs_list = line.split(" ")
        strs_list = check_word(strs_list)
        for string in strs_list:
            if string != "" and string not in strs_dict.keys():
                strs_dict[string] = 1
            elif string != "":
                strs_dict[string] += 1
    return strs_dict



print(word_count("sample.txt"))
