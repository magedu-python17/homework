#!/usr/bin/env python



def bubble_search_func(data_list):
    cnt_num_all = len(data_list)
    for i in range(cnt_num_all-1):
        for j in range(1,cnt_num_all-i):
            if(data_list[j-1]>data_list[j]):
                data_list[j-1],data_list[j]=data_list[j],data_list[j-1]



data_list = [54, 25, 93, 17, 77, 31, 44, 55, 20, 10]
bubble_search_func(data_list)
print(data_list)


