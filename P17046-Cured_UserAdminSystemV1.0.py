'''
实现一个用户管理系统，可以与管理员用户进行交互（本次先不实现验证密码之类的），根据用户输入的指令(增删改查)，可以进行相应的操作：
1.输入delete，则让用户输入”用户名”格式字符串，根据用户名查找内存里面的数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在;
2.输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找内存中数据，若存在数据则将改数据更新数据，若用户数据不存在，
则提示不存在;
3. 用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找内存中数据包
含输入字符串的用户信息，并打印;
4.用户输入list，则打印所有用户信息;打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;
5.用户输入exit，则提示用户并且保存已经修改的用户信息，退出程序;
注意：首次运行时候或者用户为0的时候，需提示用户先添加数据。
'''

#定义变量：用户信息列表，以“用户｜年龄｜联系方式”整体为元素；
UserNameInfoList = []

#定义变量：用户列表，以用户为元素；
UserNameList = []

#定义函数：列出命令，列出当前所有用户信息；无用户时，提示先添加用户；有用户时，列出当前所有用户信息；
def CmdList():
    if len(UserNameInfoList) == 0:
        NameInfoToAdd = input("No user info datas , plz enter username, age, and contract info, use ':' as separators. For example, Trump:72:White House,202-456-1111 >>>>> ")
        UserNameInfoList.append(NameInfoToAdd)
        print(UserNameInfoList)
        UserNameList.append(UserNameInfoList[-1].partition(":")[0])
        print(UserNameList)
    else:
        print("Username infos ...")
        for i in UserNameInfoList:
            print(i)

#定义函数：添加命令，添加用户信息；
def CmdAdd():
    NameInfoToAdd = input("Plz enter username, age, and contract info, use ':' as separators. For example, Trump:72:White House,202-456-1111 >>>>> ")
    UserNameInfoList.append(NameInfoToAdd)
    print(UserNameInfoList)
    UserNameList.append(UserNameInfoList[-1].partition(":")[0])
    print(UserNameList)

#主程序；
while True:
    InputCmd = input("Plz choose an option of commands : such as |add|delete|update|find|list|exit| >>>>> ")
    if InputCmd == "exit":
        print("The system is going to save datas and exit,bye.")
        exit()
    elif InputCmd == "list":
        CmdList()
    elif InputCmd == "add":
        CmdAdd()
    elif InputCmd == "delete":
        pass
    elif InputCmd == "update":
        pass
    elif InputCmd == "find":
        pass
    else:
        print("Incorrect input ! ")
    continue

#程序功能说明：exit、list、add功能实现，delete、update、find涉及迭代部分依然未调试成功。

"""
def CmdDel():
    NameToDel = input("Plz enter username your want to delete: >>>>> ")
    if NameToDel in UserNameList:
        UserNameList.remove(NameToDel)
    for i in range(len(UserNameInfoList)):
        if UserNameInfoList[i].startswith("NameToDel"):
            UserNameInfoList.remove(UserNameInfoList[i])
            print("The user info deletion completed. ")
        else:
            print("The user name you input does't exist. ")

def CmdUpdate():
    NameInfoToUpdate = input("Plz enter infos you want to update in format 'username:age:contract'. For example, Trump:72:White House,202-456-1111 >>>>> ")
    if NameInfoToUpdate in UserNameInfoList:
        for i in range(len(UserNameInfoList)):
            if UserNameInfoList[i] == NameInfoToUpdate:

        print("The user info updatition completed. ")
    else:
        print("The user name you input does't exist. ")

def CmdFind():
    NameToFind = input("Plz enter username your want to find: >>>>> ")
    if NameToFind in UserNameList:
        print(UserNameInfoList[i])
    else:
        print("The user name you input does't exist. ")
"""

def CmdList():
    if len(UserNameInfoList) == 0:
        NameInfoToAdd = input("No user info datas , plz enter username, age, and contract info, use ':' as separators. For example, Trump:72:White House,202-456-1111 >>>>> ")
        UserNameInfoList.append(NameInfoToAdd)
        print(UserNameInfoList)
        UserNameList.append(UserNameInfoList[-1].partition(":")[0])
        print(UserNameList)
    else:
        print("Username infos ...")
        for i in UserNameInfoList:
            print(i)
def CmdAdd():
    NameInfoToAdd = input("Plz enter username, age, and contract info, use ':' as separators. For example, Trump:72:White House,202-456-1111 >>>>> ")
    UserNameInfoList.append(NameInfoToAdd)
    print(UserNameInfoList)
    UserNameList.append(UserNameInfoList[-1].partition(":")[0])
    print(UserNameList)

UserNameInfoList = []
UserNameList = []
while True:
    InputCmd = input("Plz choose an option of commands : such as |add|delete|update|find|list|exit| >>>>> ")
    if InputCmd == "exit":
        print("The system is going to save datas and exit,bye.")
        exit()
    elif InputCmd == "list":
        CmdList()
    elif InputCmd == "add":
        CmdAdd()
    elif InputCmd == "delete":
        pass
    elif InputCmd == "update":
        pass
    elif InputCmd == "find":
        pass
    else:
        print("Incorrect input ! ")
    continue
