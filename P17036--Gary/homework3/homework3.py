#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/12/12'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

# 导入相关的模块
import time
import random
import datetime
import os,sys
import operator

# 定义保存用户信息的数据类型，字典中嵌套列表
dic_name = {}
# 定义一个临时文件及临时保存用户信息字典
dict_name_temp = {}
# 用户数据信息保存在文件中
file_name = 'userinfo.txt'
file_userinfo = 'password.txt'

# 获取当前系统的时间
st = datetime.datetime.now()

# 注册登录账户及密码
def register():
    # 先判断用户是否注册
    with open(file_userinfo,'r+') as f:
        res = f.readline()
        if len(res) > 0:
            return True

    print('欢迎你注册使用!')
    user,password = input('请输入用户名及密码，用空格分开').split(' ')
    with open(file_userinfo,'w+') as f:
        f.write(user+' '+password)
    print('注册完成!')
    # return False

# 管理员登录验证   账户：admin   密码：123456
def login():
    count = 0
    print('您还没有登录，请登录>>>')
    with open(file_userinfo,'r') as f:
        user,password = f.readline().split(' ')
    while count <3:
        admin_name,admin_password = input('请输入用户名及密码,用空格分开>>>').split(' ')
        if admin_name == user and admin_password == password:
            print('登录成功!')
            return True
        else:
            print('用户名及密码输入错误!')
            count +=1
    return False

# 读文件里面的信息
# 判断文件里面的数据是否为空
#为空就首先添加数据
def read_file():
    try:
        with open(file_name,'r') as f:
            res = f.read()
            if len(res) >0:
                return False
            else:
                # register()
                return True
    except FileNotFoundError:
        # register()
        print('文件不存在')
        os.mkdir(file_name)
        return True

# 用户界面
def menu():
    print('欢迎进入用户管理系统'.center(60,'*'))
    print('当前时间:{}-{}-{} {}:{}:{}   星期    {}'.format(st.year,st.month,st.day,st.hour,st.minute,st.second,st.weekday()).center(60,' '))
    print(''.center(70,'*'))
    print('delete:删除用户  '.center(60,' '))
    print('update:更新用户的数据'.center(60,' '))
    print('find:查找用户     '.center(60,' '))
    print('list:显示用户信息  '.center(60,' '))
    print('add:添加用户信息  '.center(60,' '))
    print('exit:退出      '.center(60,' '))
    print(''.center(70,'*'))

# 查看函数    查看并排序
#默认按name排序
#可以指定字段排序
def list_user():
    user_order = []
    user_temp = []
    print('查到的信息如下...')
    print('用户名    年龄    联系方式')
    with open(file_name,'r') as f:
        for line in f.readlines():
            user_name,user_age,user_phonenumber = line.split(' ')
            # print(user_name,user_age,user_phonenumber)
            # print(type(line))
            user_temp.append(user_name)
            user_temp.append(user_age)
            user_temp.append(user_phonenumber)
            user_order.append(user_temp)
            user_temp = []

    mode = input('请输入按照什么字段排序:name,age or phone>>>')
    if mode == 'name':
        user_order.sort(key=lambda x:str(x[0]))

    elif mode == 'age':
        user_order.sort(key=lambda x:int(x[1]))

    elif mode =='phone':
        user_order.sort(key=lambda x:int(x[2]))

    # print(user_order)
    cnt = 0

    for i in user_order:
        if cnt == 0:
            print('用户名    年龄    联系方式')
        # print(type(i))
        cnt += 1
        print('{}  {}  {}'.format(i[0],i[1],i[2]))
        # print('\n')

#删除用户
def delete_user():
    ret = 0
    flag = False
    list_name_temp = []
    name = input('请输入用户名>>')
    with open(file_name,'r') as f:
        for line in f.readlines():
            user_name,user_age,user_phonenumber = line.split(' ')
            if name == user_name:  #删除用户信息
                flag = True
                time.sleep(random.randint(2,4))
                print('正在把{}从系统中删除'.format(name))
            else:
                list_name_temp.append(line)  #把每行数据添加到列表中
                dict_name_temp[ret] = list_name_temp
                list_name_temp = []  #清空列表
                ret +=1

    #把字典里的数据写入到文件中
    with open(file_name,'w') as f:
        for k,v in dict_name_temp.items():
            user_str = str(v).replace("['","").replace("\\n']","")
            f.write(user_str)
            f.write('\n')

    # dict_name_temp = {}

    #没有此用户的信息
    if flag == False:
        time.sleep(random.randint(6,9))
        print('哎呦，我都跑到火星上找了，还是没有找到您要删除的用户信息...')
    else:
        print('信息删除成功!')

 #添加用户
def add_user():
    username,age,phone_number = input('请输入用户名，年龄及联系方式，用空格分开>>').split(' ')
    print('添加的信息如下...')
    print('用户名:{}    年龄:{}    手机号码:{}'.format(username,age,phone_number))
    st1 =username + ' '+ age + ' ' + phone_number
        #把用户的信息保存在文件中
    with open(file_name,'a+') as f:
        f.write(st1)
        # f.write('\n')
    print('添加信息成功!')

#查找用户
def search_user():
    name = input('请输入用户名>>')
    flag = False
    user_temp = [] #存储临时信息
    with open(file_name,'r') as f:
        for line in f.readlines():
            user_name,user_age,user_phonenumber = line.split(' ')
            if user_name == name:
                flag = True
                user_temp.append(user_name)
                user_temp.append(user_age)
                user_temp.append(user_phonenumber)

    if flag:
        time.sleep(random.randint(1,3))
        print('系统里面有您要查找的用户信息...')
        print('查到的信息如下...')
        print('用户名    年龄    联系方式')
        print('{}    {}     {}'.format(user_temp[0],user_temp[1],user_temp[2]))

    else:  #找不到用户的信息
        time.sleep(random.randint(2,5))
        print('哎呦，我都跑到火星上找了，还是没有找到您要找的用户信息...')

#更新用户信息
def update_user():
    list_name_temp = []
    flag = False
    ret = 0
    username,age,phone_number = input('请输入用户名，年龄及联系方式').split(' ')
    with open(file_name,'r') as f:
        for line in f.readlines():
            # print(line.split(' '))
            if line != '\n':
                user_name,user_age,user_phonenumber = line.split(' ')
                if user_name == username: #找到用户的信息
                    print('开始更新信息...')
                    flag = True
                    lin = username+' '+age +' ' + phone_number +'\n'
                    list_name_temp.append(lin)
                    dict_name_temp[ret] = list_name_temp
                    list_name_temp = []

                else:
                    list_name_temp.append(line)  #把每行数据添加到列表中
                    dict_name_temp[ret] = list_name_temp
                    list_name_temp = []  #清空列表
            ret +=1

    # print('打印字典')
    # print(dict_name_temp)

    #把字典里的数据写入到文件中
    with open(file_name,'w') as f:
        # pass
        for k,v in dict_name_temp.items():
            user_str = str(v).replace("['","").replace("\\n']","")
            f.write(user_str)
            f.write('\n')

        #没有此用户的信息
    if flag == False:
        time.sleep(random.randint(6,9))
        print('哎呦，我都跑到火星上找了，还是没有找到您要找的用户信息...')
    else:
        print('更新信息成功!')

# 主函数
def main():
    #先判断用户是否注册了账户及密码
    register()

    while True:
        menu()
        # 判断文件是否为空及是否存在
        if read_file():
                print('系统暂时没有用户信息，请添加信息！')
                username,age,phone_number = input('请输入用户名，年龄及联系方式，用空格分开>>').split(' ')
                # 把用户信息保存在一个临时列表中，把临时列表信息添加到字典中
                ls_temp = [age,phone_number]
                dic_name[username] = ls_temp
                print('添加的信息如下...')
                str = username + ' '+ age+ ' '+ phone_number
                #把用户的信息保存在文件中
                with open(file_name,'a+') as f:
                    f.write(str)
                    f.write('\n')
        else:
            choise_number = input('请输入你想要操作的选项>>')

            # 删除用户信息
            if choise_number.lower() == 'delete':
                if login():
                    delete_user()
                else:
                    print('输入次数超限，程序退出...')

            elif choise_number.lower() == 'update':
                if login():
                    update_user()
                else:
                    print('输入次数超限，程序退出...')

            elif choise_number.lower() == 'find':
                if login():
                    search_user()
                else:
                    print('输入次数超限，程序退出...')

            elif choise_number.lower() == 'list':
                if login():
                    list_user()
                else:
                    print('输入次数超限，程序退出...')

            elif choise_number.lower() == 'exit':

                print('您已经保存了修改的数据，谢谢您本次的使用,期待您再一次的使用！')
                exit()

            elif choise_number.lower() == 'add':  #添加用户信息
                if login():
                    add_user()
                else:
                    print('输入次数超限，程序退出...')

if __name__=="__main__":
    main()
# 可以，看到有些地方已经抽象出来了，sys和 operator 没有用到的话 可以删除