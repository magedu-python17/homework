#!/usr/bin/env python

def foo1(dict_name,newkey="",new_dict={}):
    if type(dict_name) == dict:
        for key in dict_name:
            if newkey != "":
                tmpkey = newkey + "." + key  
            else:
                tmpkey = newkey + key
            foo1(dict_name[key],tmpkey)
    else:
        new_dict[newkey] = dict_name
    return new_dict

dict1 = {'a':{'b':{'g':5},'c':2},'d':{'e':3,'f':4}}
print(foo1(dict1))

