'''
实现一个用户管理系统，可以与管理员用户进行交互(本次先不实现验证密码之类的)，
根据用户输入的指令(增删改查)，可以进行相应的操作：
 比如 1.输入delete，则让用户输入”用户名”格式字符串，根据用户名查找内存里面的数据，
 若存在数据则将该数据移除，若用户数据不存在，则提示不存在;
 2.输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，
 根据用户名查找内存中数据，若存在数据则将改数据更新数据，若用户数据不存在，
 则提示不存在;
 3. 用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找内存中数据包
 含输入字符串的用户信息，并打印;
 4.用户输入list，则打印所有用户信息;打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;
 5.用户输入exit，则提示用户并且保存已经修改的用户信息，退出程序；
 注意：首次运行时候或者用户为0的时候，需提示用户先添加数据。
 '''

"""
 在第一次的作业基础上，增加以下功能
 1.用户信息保存
 2.排序：可以让用户指定排序字段，默认name 排序
 3.增加管理员验证功能(即首次运行系统时候，提示管理员设置密码，
 用户进行 add list delete update find的时候需要验证管理员密码)
 """


import json
import os
import getpass
os.system('''[ ! -f test.txt ] && echo '{}' > test.txt''')
'''
对函数还不是很了解,大概知道json会把字典保存到文件中去，
程序刚启动时是没有这个文件的，所以判断文件不
存在的话，生成一个并echo一空字典
'''
file = open('test.txt', 'r')
js = file.read()
dic = json.loads(js)
file.close()

passwd = None
if not passwd:
    passwd = getpass.getpass('set password>>>')

def passwd_f(): # 定义密码函数以后使用
    while True:
        _ = getpass.getpass('input password>>')
        if _ == passwd:
            break
        else:
            print('wrong')
            continue


passwd_f()

while True:
    if dic == {}:  # 如果字典里没有数据，让用户输入信息并分别追加到字典
        while True:  # 次循环是为了能够让用户接着添加数据
            print("Please add data>>>")
            name, age, contact = input('format: < name:age:contact >  #').split(':')
            dic[name] = [age, contact]
            print(dic)
            choice = input('continue? Yy|Nn')
            if choice.lower() == 'y':
                continue
            else:
                break

# 字典有数据后提示用户键入命令
    else:
        print('start your service>>>')
        print('options: delete/update/find/list/sort/exit')
        command = input('cmd# ')
# ________________________

        if command == 'delete':
            passwd_f()
            print('enter the user you want to delete>>>')
            tmp_name = input('delete# ')  # 临时变量存着用户要删除的用户
            if tmp_name in dic: # 判断用户是否在字典中
                del dic[tmp_name]
                print('delete {} successfully'.format(tmp_name))
            else:
                print('user not exist')


        if command == 'update':
            passwd_f()
            print('enter this format: username:age:contact  >>>')
            tmp_ = input('update# ')
            tmp_name = tmp_.split(':')[0]  # 取出用户名看其是否存在，若存在，更新另外两项
            tmp_age = tmp_.split(':')[1]
            tmp_contact = tmp_.split(':')[2]
            if tmp_name in dic:
                dic[tmp_name][0] = tmp_age
                dic[tmp_name][1] = tmp_contact
                print('update {} successfully'.format(tmp_name))
            else:
                print('no such user')


        if command == 'find':
            passwd_f()
            print('input a user name>>>')
            tmp_name = input('find# ')
            if tmp_name in dic:
                print(dic[tmp_name])
            else:
                print('no such user')


        if command == 'list':
            passwd_f()
            print('{} {:>5} {:>10}'.format('user', 'age', 'contact'))
            for i in dic:
                print('  {} {:>5} {:>10}'.format(i, dic[i][0], dic[i][1]))

        if command == 'sort':
            passwd_f()
            print(sorted(dic.items(), key=lambda d: d[0]))
            choice = input('sortord: <age/contact>')
            if choice == 'age':
                print(sorted(dic.items(), key=lambda dic: dic[1][0]))
            if choice == 'contact':
                print(sorted(dic.items(), key=lambda dic: dic[1][1]))


        if command == 'exit':  # 把字典保存到文件
            js = json.dumps(dic)
            file = open('test.txt', 'w')
            file.write(js)
            file.close()
            break

