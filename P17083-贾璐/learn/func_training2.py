#!/usr/bin/env python

def left_print(*args):
    lst_init = list(args)
    #length_init = len(lst_init)
    str_lenth_init = len(" ".join(list(str(x) for x in lst_init)))
    while len(lst_init) > 0:
        lst = list(reversed(lst_init))
        #if len(lst) == length_init:
        str_line = " ".join(list(str(x) for x in lst))
        print("{0:>{1}}".format(str_line,str_lenth_init))
        #else:
            #print(" " * (length_init - len(lst)) + " ".join(list(str(x) for x in lst)))
        lst_init.pop()

def right_print(*args):
    lst_init = list(reversed(list(args)))
    length_init = len(lst_init)
    str_lenth_init = len(" ".join(list(str(x) for x in lst_init)))
    for i in range(length_init):
        str_line = " ".join(list(str(x) for x in lst_init[(length_init - i - 1):length_init]))
        print("{0:>{1}}".format(str_line,str_lenth_init))
    

num = int(input("Enter a number: "))

lst = range(1,num+1)

left_print(*lst)
#right_print(*lst)
    
