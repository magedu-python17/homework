

# -*- coding:utf8 -*-
"""
Created on:
@author: VeRy.Zly
Email: 18321960026@139.com
Version: V.2018.12.16-V0
Description:第一周作业
Demand:
实现一个用户管理系统，可以与管理员用户进行交互，根据用户输入的指令(增删改查)，可以进行相应的操作：
1.输入delete，则让用户输入”用户名”格式字符串，根据用户名查找内存里面的数据，
若存在数据则将该数据移除，若用户数据不存在，则提示不存在;

2.输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找内存中数据，
若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在;

3. 用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找内存中数据包含输入字符串的用户信息，并打印;

4.用户输入list，则打印所有用户信息;打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;

5.用户输入exit，则提示用户并且保存已经修改的用户信息，退出程序;

注意：首次运行时候或者用户为0的时候，需提示用户先添加数据。

"""
"""
使用open函数读取数据源
"""
file_wr = open(r"D:\magepython\ums.txt", "a+")
file_r = open(r"D:\magepython\ums.txt")
user_lst = file_r.readlines()

def get_help():
    """
    通过"help"命令查看可以操作的命令
    :return:
    """
    CliSet = '''
        add --to add new user when first use this manage system
        delete --to delete user
        update --to update user Information
        find --to find user 
        list --to show all user Information
        exit --to quit 
    '''
    print("{}".format(CliSet))

def add():
    """
    添加用户信息，包括名字，年龄，联系方式
    :return:
    """
    if len(user_lst) == 0:
        file_wr.write("name :age :contact")
    print("please enter new user")
    name = str(input("name:"))
    age = int(input("age:"))
    contact = int(input("contact:"))
    b_add = "\n{:<5}:{:<4}:{}".format(name, age, contact)
    file_wr.write(b_add)
    file_wr.close()

def delete():
    """
    通过输入用户名进行查找，存在即删除，否则提示不存在
    备注：删除和保存一起做了，可以把保存部分单独实现
    :return:
    """
    file_w = open(r"D:\magepython\ums.txt", "w")
    name = input("Please enter name:")
    for user_num in range(len(user_lst)):
        if name in user_lst[user_num]:
            user_lst.pop(user_num)
            file_w.writelines(user_lst)
            file_w.close()
            break
    else:
        print("this user not exist")

def update():#更新用户
    """
    通过输入用户名:年龄:联系方式，使用用户名与现有数据进行对比，若存在更新，否则不存在
    :return:
    """
    file_w = open(r"D:\magepython\ums.txt", "w")
    _user = input("please enter 用户名:年龄:联系方式:")
    _lst = _user.split(":")
    new_lst = "{:<5}:{:<4}:{}".format(_lst[0], _lst[1], _lst[2])
    for user_num in range(len(user_lst)):
        if _lst[0] in user_lst[user_num]:
            user_lst[user_num] = new_lst
            file_w.writelines(user_lst)
            file_w.close()
            break
    else:
        print("this user not exist")

def find():
    """
    通过用户名查看此用户所有信息
    :return:
    """
    name = input("Please enter name:")
    for user_num in range(len(user_lst)):
        if name in user_lst[user_num]:
            print(user_lst[user_num])
            break
    else:
        print("this user not exist")

def lst():
    """
    查看所有用户信息
    :return:
    """
    for i in user_lst:
        i = i.strip("\n")
        print(i)

def exit():
    """
    退出用户管理系统！
    :return:
    """
    print("thank you fou using ，goodbye!")

if __name__ == "__main__":
    if len(user_lst) == 0:
        print("Welcome to first user manage system,you can enter help command")
    command = input("Please enter the command:")
    if command == "help":
        get_help()
    elif command == "delete":
        delete()
    elif command == "update":
        update()
    elif command == "find":
        find()
    elif command == "add":
        add()
    elif command == "list":
        lst()
    elif command == "exit":
        exit()
    else:
        print("your enter command error!")

# 尝试用while True 试下，正常来说，一个操作系统，应该有用户来选择操作的，而不是运行一次就结束