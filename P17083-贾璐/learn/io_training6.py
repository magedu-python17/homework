#!/usr/bin/env python

i_list = ["!",",",".","?","/","[","]"]
list1 = [x for x in (lambda *args:map(lambda x:str(x),args))(*range(5))]





def cope_file(filename1,filename2):
    list2 = []
    with open(filename1,"r") as f:
        for line in f.readlines():
            list2.append(line)
    with open(filename2,"w+") as f:
        f.writelines(list2)




