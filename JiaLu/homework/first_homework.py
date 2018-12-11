#!/usr/bin/env python
import os
import readline
def open_file(use_mode,user_info):
    file_path = input("Please enter your user_info file path: ")
    if file_path == "":
        file_path = "/home/python/python_projects/3.5.3/homework/JiaLu/homework/user_info"
    if use_mode == "open":
        if os.path.exists(file_path):
            mode = 'r+'
            f = open(file_path,mode)
            user_info = eval(f.readline())
            f.close()
        else:
            mode = 'a+'
            f = open(file_path,mode)
            f.close()
            user_info = []
        return user_info
    elif use_mode == "save":
            mode = 'w+'
            f = open(file_path,mode)
            f.write(str(user_info))
            f.close()


def delete_user():
    print("Please enter user's username to delete: ")
    user_name = input(">>> ")
    for index in range(len(user_info)):
        if user_info[index]["user_name"] == user_name:
            del user_info[index]
            break
    else:
        print("The user does not exist!")

def add_user(user_info):
    print("Please enter user's infomation like this: \n    username:age:contact infomation")
    user_input = input(">>> ")
    user_name = user_input.split(":")[0]
    for item in user_info:
        if item["user_name"] == user_name:
            print("The user does exist! Please use the 'update' command to update existing user information!")
            break
    else:
        user_age = user_input.split(":")[1]
        user_contact = user_input.split(":")[2]
        user_info.append({"user_name":user_name,"user_age":user_age,"user_contact":user_contact})

def search_user():
    print("Please enter user's username to search: ")
    user_name = input(">>> ")
    for index in range(len(user_info)):
        if user_info[index]["user_name"] == user_name:
            print(user_info[index])
            break
    else:
        print("The user does not exist!")

def update_user():
    print("Please use the following format to update user information: \n    username:age:contact infomation")
    user_input = input(">>> ")
    user_name = user_input.split(":")[0]
    for index in range(len(user_info)):
        if user_info[index]["user_name"] == user_name:
            user_age = user_input.split(":")[1]
            user_contact = user_input.split(":")[2]
            user_info[index] = {"user_name":user_name,"user_age":user_age,"user_contact":user_contact}
            print(user_info[index])
            break
    else:
        print("The user does not exist!")

def list_user(user_info):
    print("{:<5}:  {:<10}  |  {:<10}  |  {:<10}  ".format("field","user_name","user_age","user_contact"))
    #print("field : user_name | user_age | user_contact")
    print("{:<5}:  {:<10}  |  {:<10}  ".format("sort","reverse","default"))
    #print("sort : reverse | default")
    mode = input("Please enter how you want to sort and by field (format: field sort): ")
    field = mode.split(" ")[0]
    sort_mode = mode.split(" ")[1]
    if sort_mode == "reverse":
        new_user_info = sorted(user_info,key=lambda x:x[field],reverse=True)
    else:
        new_user_info = sorted(user_info,key=lambda x:x[field])
    print("{:<30}    |    {:<30}    |    {:<30}    ".format("username","age","contact"))
    for item in new_user_info:
        print("{:<30}    |    {:<30}    |    {:<30}".format(item["user_name"],item["user_age"],item["user_contact"]))

def get_help():
    strings = "            help ------ get command help list\n \
           add ------ add an new user\n \
           delete ------ delete a user\n \
           find ------ find a user's infomation\n \
           update ------ update a user's infomation\n \
           list ------ print all user's information\n \
           exit ------ exit this user management system\n \
        "
    print("{}".format(strings))

def exit_system():
    print("Thank you use this user management system! Bye bye!")



init_info = [{}] 
user_info = open_file("open",init_info)
print("Welcome to use this user management system! You can enter 'help' to get help!")
while True:
    count = len(user_info)
    if count == 0:
        print("Please add an new user first! ")
    command = input("Command > ")
    if command == "help":
        get_help()
    elif command == "add":
        add_user(user_info)
    elif command == "delete":
        delete_user()
    elif command == "find":
        search_user()
    elif command == "list":
        list_user(user_info)
    elif command == "update":
        update_user()
    elif command == "exit":
        open_file("save",user_info)
        exit_system()
        break
    else:
        print("Wrong Command!")   
