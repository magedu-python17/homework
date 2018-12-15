#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: zhide.zhang
user_list=[]
up_list=[]
a = 0
while a < 3:
    enter = input("请输入push、delete、find、update、list、exit指令>>> ")
#    user_list = []
    if enter == "push":
        b = input("请输入姓名:年龄:联系方式;并以冒号分隔>>>")
        if b.count(':') == 2:
            user_list.append(b.split(":"))
        else:
            print("error")
###########################################################
    elif enter == "delete":
        if len(user_list) == 0:
            print("请先添加数据")
            b = input("请输入姓名:年龄:联系方式;并以冒号分隔>>>")
            if b.count(':') == 2:
                user_list.append(b.split(":"))
            else:
                print("error")
        else:
            delete_list = input("please enter delete name>>> ")
            for d in range(len(user_list)):
                if delete_list == user_list[d][0]:
                    user_list.remove(user_list[d])
                    break
            else:
                print("该用户不存在")
##############################################
    elif enter == "update":
        if len(user_list) == 0:
            print("请先添加数据")
            b = input("请输入姓名:年龄:联系方式;并以冒号分隔>>>")
            if b.count(':') == 2:
                user_list.append(b.split(":"))
            else:
                print("error")
        else:
            up = input("请输入需要更新的用户名:年龄:联系方式>>>")
            if up.count(':') == 2:
                up_list = up.split(":")
                for i in range((len(user_list))):
                    if user_list[i][0] == up_list[0]:
                        user_list[i][1] = up_list[1]
                        user_list[i][2] = up_list[2]
                        break
                else:
                    print("该用户不存在")
            else:
                print("error")

####################################
    elif enter == "find":
        if len(user_list) == 0:
            print("请先添加数据")
            b = input("请输入姓名:年龄:联系方式;并以冒号分隔>>>")
            if b.count(':') == 2:
                user_list.append(b.split(":"))
            else:
                print("error")
            print(user_list)
        else:
            find_name = input("请输入要查找的姓名>>>")
            for x in range(len(user_list)):
                if user_list[x][0] == find_name:
                    #print(user_list[x])
                    print("age:",user_list[x][1],"\n","number:",user_list[x][2])
                    break
            else:
                print("该用户不存在")

########################################################
    elif enter == "list":
        if len(user_list) == 0:
            print("请先添加数据")
            b = input("请输入姓名:年龄:联系方式;并以冒号分隔>>>")
            if b.count(':') == 2:
                user_list.append(b.split(":"))
            else:
                print("error")
            #print(user_list)
        else:
            print('{:10} {:10} {:10}'.format("name", "age", "number"))
            for i in range(len(user_list)):
                print('{:10} {:10} {:10}'.format(user_list[i][0], user_list[i][1], user_list[i][2]))

############################################################
    elif enter == "exit":
        if len(user_list) == 0:
            print("请先添加数据")
            b = input("请输入姓名:年龄:联系方式;并以冒号分隔>>>")
            if b.count(':') == 2:
                user_list.append(b.split(":"))
            else:
                print("error")
        elif len(up_list) == 0:
            a = 4
            print("退出")
        else:
            print("更新用户{}已经保存。".format(up_list[0]))
            a = 4
    else:
        print("please enter push/delete/update/find/exit")
