#!/usr/bin/env python
import os
def list_create(list_name,list_dict):
    list_set = list(set(list_name))
    for i in list_set:
        for j in list_name:
            if i == j:
                list_dict[i] += 1
    keys = list_dict.keys()
    values = list_dict.values()
    list_one = [(key,val) for key,val in zip(keys,values)]
    list_sort = sorted(list_one,key=lambda x:x[1],reverse=True)
    list_return = []
    if len(list_sort) >= 10:
        for i in range(10):
            list_return.append(list_sort[i])
    else:
        for i in range(len(list_sort)):
            list_return.append(list_sort[i])
    return list_return
    
def open_file(output_type):    #用户数据文件读取＆写入
    #输入用户信息文件读取存放绝对路径---需要带文件名
    ip_dict = {}
    ip_list = []
    ip_count = 0
    url_dict = {}
    url_list = []
    url_count = 0
    status_code_dict = {} 
    status_code_list = []
    status_code_count = 0
    file_path = input("Please enter your user_info file path: ")
    if file_path == "":     #如果不输入就采用默认路径
        file_path = "/home/python/python_projects/3.5.3/homework/P17083-贾璐/learn/access.log"
    if os.path.exists(file_path):    #如果文件存在
        mode = 'r+'    #模式是r+   就是打开文件读取文件
        f = open(file_path,mode)    #以r+模式打开文件
        for i in f.readlines():
            if output_type == "ip":
                ip_list.append(i.split(" ")[0])
                ip_dict[i.split(" ")[0]] = 0
            elif output_type == "url":
                url_list.append(i.split(" ")[6])
                url_dict[i.split(" ")[6]] = 0
            elif output_type == "status_code":
                status_code_list.append(i.split(" ")[8])
                status_code_dict[i.split(" ")[8]] = 0 
        f.close()    #关闭文件
    if output_type == "ip":
        new_ip_list = list_create(ip_list,ip_dict)
        print(new_ip_list)
    elif output_type == "url":
        new_url_list = list_create(url_list,url_dict)
        print(new_url_list)
    elif output_type == "status_code":
        new_status_code_list = list_create(status_code_list,status_code_dict)
        print(new_status_code_list)

open_file("status_code")
