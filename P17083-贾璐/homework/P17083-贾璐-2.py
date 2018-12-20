#!/usr/bin/env python
import os
import readline
import getpass



def check_null(str1):
    if str1 == "" or str1.count(":") != 3:
        return False
    else:
        return True
def check_null2(str1):
    if str1 == "":
        return False
    else:
        return True

def open_file(use_mode,user_info):    #用户数据文件读取＆写入
    #输入用户信息文件读取存放绝对路径---需要带文件名
    file_path = input("Please enter your user_info file path: ")
    if file_path == "":     #如果不输入就采用默认路径
        file_path = "/home/python/python_projects/3.5.3/homework/P17083-贾璐/homework/user_info"
    if use_mode == "open":   #如果用户模式是open，就执行下面代码
        if os.path.exists(file_path):    #如果文件存在
            mode = 'r+'    #模式是r+   就是打开文件读取文件
            f = open(file_path,mode)    #以r+模式打开文件
            user_info = eval(f.readline())   #逐行读取并转换成对应数据结构如果是{}就读成字典，如果是[]就读成列表
            f.close()    #关闭文件
        else:     #如果文件不存在
            mode = 'a+'    #模式是a+   创建不存在的文件
            f = open(file_path,mode)
            f.close()
            user_info = []  #令user_info为[]
        return user_info    #返回user_info的值
    elif use_mode == "save":    #如果模式是save就执行下面代码
            mode = 'w+'     #模式是w+   打开文件并更改文件内容
            f = open(file_path,mode)
            f.write(str(user_info))   #将user_info里的内容转换成字符串并写入到指定文件中去
            f.close()


def delete_user():      #删除用户
    print("Please enter user's username to delete: ")    #提示信息
    user_name = input(">>> ")   #将用户输入的用户名赋值给user_name变量
    if check_null2(user_name):
        for index in range(len(user_info)):     #将用户信息遍历
            if user_info[index]["user_name"] == user_name:    #找出符合的用户
                del user_info[index]   #删除这个用户信息
                break    #跳出循环
        else:    #如果用户不存在就执行下面代码
            print("The user does not exist!")
    else:
        print("Please input the user_name!")

def add_user(user_info):    #添加用户
    print("Please enter user's infomation like this: \n    username:age:contact infomation") #提示信息
    user_input = input(">>> ")    #将用户输入的用户信息赋值给user_input
    if check_null(user_input):
        user_name = user_input.split(":")[0]   #分片出用户名
        for item in user_info:   #遍历user_info
            if item["user_name"] == user_name:   #如果用户存在执行下面代码并跳出循环
                print("The user does exist! Please use the 'update' command to update existing user information!")
                break
        else:    #用户不存在的话执行下面代码
            user_age = int(user_input.split(":")[1])
            user_contact = int(user_input.split(":")[2])
            user_info.append({"user_name":user_name,"user_age":user_age,"user_contact":user_contact})
    else:
        print("Please input the command!")

def search_user():   #查找用户
    print("Please enter user's username to search: ")
    user_name = input(">>> ")
    if check_null2(user_name):
        for index in range(len(user_info)):
            if user_info[index]["user_name"] == user_name:
                print(user_info[index])
                break
        else:
            print("The user does not exist!")
    else:
        print("Please input the user_name!")

def update_user():    #更新用户信息
    print("Please use the following format to update user information: \n    username:age:contact infomation")
    user_input = input(">>> ")
    if check_null(user_input):
        user_name = user_input.split(":")[0]
        for index in range(len(user_info)):
            if user_info[index]["user_name"] == user_name:
                user_age = int(user_input.split(":")[1])
                user_contact = int(user_input.split(":")[2])
                user_info[index] = {"user_name":user_name,"user_age":user_age,"user_contact":user_contact}
                print(user_info[index])
                break
        else:
            print("The user does not exist!")
    else:
        print("Please input the command")

def list_user(user_info):   #列出所有用户信息并根据指定字段进行升序/降序排序
    print("{:<5}:  {:<15}  |  {:<15}  |  {:<15}  ".format("field","[user_name]","user_age","user_contact"))
    #print("field : user_name | user_age | user_contact")
    print("{:<5}:  {:<15}  |  {:<15}  ".format("sort","reverse","[default]"))
    #print("sort : reverse | default")
    mode = input("Please enter how you want to sort and by field (format: field sort): ")
    if mode != "":
        field = mode.split(" ")[0]
        sort_mode = mode.split(" ")[1]
    else:
        field = "user_name"
        sort_mode = "default"
    if sort_mode == "reverse":
        new_user_info = sorted(user_info,key=lambda x:x[field],reverse=True)
    else:
        new_user_info = sorted(user_info,key=lambda x:x[field])
    print("{:<30}    |    {:<30}    |    {:<30}    ".format("username","age","contact"))
    for item in new_user_info:
        print("{:<30}    |    {:<30}    |    {:<30}".format(item["user_name"],item["user_age"],item["user_contact"]))

def get_help():   #获取帮助
    strings = "            help ------ get command help list\n \
           add ------ add an new user\n \
           delete ------ delete a user\n \
           find ------ find a user's infomation\n \
           update ------ update a user's infomation\n \
           list ------ print all user's information\n \
           exit ------ exit this user management system\n \
        "
    print("{}".format(strings))

def exit_system():  #退出系统
    print("Thank you use this user management system! Bye bye!")

def set_passwd(func,password,file_path):
    if func == "set":
        mode = 'w+'
        f = open(file_path,mode)
        f.write(password)
        f.close()
    elif func == "read":
        mode = 'r+'
        f = open(file_path,mode)
        user_password = f.readline()
        f.close()
        return user_password

def check_passwd(password):
    passwd = getpass.getpass("Please input your admin password: ")
    if passwd == password:
        return True
    else:
        return False

def check_passwd_file(file_path):
    if os.path.exists(file_path):
        return True
    else:
        file_path = input("Please input your user_password file path: ")
        if os.path.exists(file_path):
            return file_path
        else:
            mode = 'a+'
            f = open(file_path,mode)
            f.close()
            return file_path
init_info = [{}] 
user_info = open_file("open",init_info)
print("Welcome to use this user management system! You can enter 'help' to get help!")
password_file = "/home/python/python_projects/3.5.3/homework/P17083-贾璐/homework/user_passwd"
file_check = check_passwd_file(password_file)
if file_check != True:
    password_file = file_check
check_password = set_passwd("read","",password_file)
if check_password == "":
    init_password = getpass.getpass("Please set your admin password: ")
    set_passwd("set",init_password,password_file)
    real_password = set_passwd("read","",password_file)
else:
    real_password = check_password
while True:
    count = len(user_info)
    if count == 0:
        print("Please add an new user first! ")
    command = input("Command > ")
    if command == "help":
        get_help()
    elif command == "add":
        flag = check_passwd(real_password)
        if flag:
            add_user(user_info)
        else:
            print("Wrong admin password!")
    elif command == "delete":
        flag = check_passwd(real_password)
        if flag:
            delete_user()
        else:
            print("Wrong admin password!")
    elif command == "find":
        flag = check_passwd(real_password)
        if flag:
            search_user()
        else:
            print("Wrong admin password!")
    elif command == "list":
        flag = check_passwd(real_password)
        if flag:
            list_user(user_info)
        else:
            print("Wrong admin password!")
    elif command == "update":
        flag = check_passwd(real_password)
        if flag:
            update_user()
        else:
            print("Wrong admin password!")
    elif command == "exit":
        open_file("save",user_info)
        exit_system()
        break
    else:
        print("Wrong Command!")   

# 贾独秀 没有毛病，就是文件名字最好以学号+姓名来命名下哈
