#定义密码*号表示
def getpass(prompt = 'Password: '):
    if p != {}:
        print('Please enter the administrator password')
    count = 0
    chars = []
    for x in prompt:
        msvcrt.putch(bytes(x,'utf8'))
    while True:
        new_char = msvcrt.getch()
        if new_char in b'\r\n':
            break
        elif new_char == b'\0x3': #ctrl + c
            raise KeyboardInterrupt
        elif new_char == b'\b':
            if chars and count >= 0:
                count -= 1
                chars =  chars[:-1]
                msvcrt.putch(b'\b')
                msvcrt.putch(b'\x20')#space
                msvcrt.putch(b'\b')
        else:
            if count < 0:
                count = 0
            count += 1
            chars.append(new_char.decode('utf8'))
            msvcrt.putch(b'*')
    print('\r')
    return ''.join(chars)

#定义密码判断
def password_judge(password):
    while True:
        if password == '' or password not in p:
            print('password error')
            password = getpass()
        else:
            break


#定义判断输入
def input_data(data):
    if data.count(":") == 2:  # 判断添加的数据的格式
        username, age, mobile = data.split(':', 2)  # 拆分成3部分 。前一部分为username为key，后两部分年龄和联系方式为age和mobile
        if username == '' or not age.isdigit() or not mobile.isdigit:  # 判断username 和age ，mobile是否符合要求
            print('data in wrong format')  # 不符合就报错
        else:
            return username, age, mobile
    else:
        print('data in wrong format')  # 不符合就报错

#定义add数据
def add_data(data):
    if data == None:
        return
    else:
        username, age, mobile = data
        if username in d:  # 符合要求就判断数据是否存在
            print('user data exist, please update')
        else:
            d[username] = [age, mobile]  # 不在就添加进去
            print('add success')


#定义delete数据
def delete_add(data):
    if data in d:  # 判断username在不在key中
        del d[data]  # 在就删除
        print('delete success')
    else:
        print(error+'or,username error')  # 不在就报错

#定义update数据
def update_data(data):
    if data == None:
        return
    else:
        username, age, mobile = data
        if username in d:  # 判断是否在d中
            d.update({username: [age, mobile]})  # 在就跟新
            print('update success')
        else:
            print(error)  # 不在就报错

#定义find数据
def find_data(data):
    if data in d:  # 判断是否在d中
        print('username    | age  |   mobile information')
        print('{:^10}{:^10}{:^20}'.format(data, d[data][0], d[data][1]))  # 打印数据
    else:
        print(error+'or,username error')

#定义list数据
def list_data(command):
    if d == {}:
        return
    print('username    | age  |   mobile information')
    for k in d:
        print('{:^10}{:^10}{:^20}'.format(k, d[k][0], d[k][1]))  # 列出来
    print('if you want to sort,please input sort command:(username or age or mobile):resrver(Ture or False)\n''if you do not want sort please input exit')

#定义sort排序
def sort_data(sortcommand):
    if sortcommand != 'exit':  # 排序的话就打印数据标题
        print('username    | age  |   mobile information')
    if sortcommand == 'username:True':  # 排序命令
        lst = sorted(d.items(), reverse=True)
        for i in range(len(lst)):  # 排序打印
            print('{:^10}{:^10}{:^20}'.format(lst[i][0], lst[i][1][0], lst[i][1][1]))
    elif sortcommand == 'username:False':
        lst = sorted(d.items(), reverse=False)
        for i in range(len(lst)):
            print('{:^10}{:^10}{:^20}'.format(lst[i][0], lst[i][1][0], lst[i][1][1]))
    elif sortcommand == 'age:True':
        lst = sorted(d.items(), key=lambda v: v[1][0], reverse=True)
        for i in range(len(lst)):
            print('{:^10}{:^10}{:^20}'.format(lst[i][0], lst[i][1][0], lst[i][1][1]))
    elif sortcommand == 'age:False':
        lst = sorted(d.items(), key=lambda v: v[1][0], reverse=False)
        for i in range(len(lst)):
            print('{:^10}{:^10}{:^20}'.format(lst[i][0], lst[i][1][0], lst[i][1][1]))
    elif sortcommand == 'mobile:True':
        lst = sorted(d.items(), key=lambda v: v[1][1], reverse=True)
        for i in range(len(lst)):
            print('{:^10}{:^10}{:^20}'.format(lst[i][0], lst[i][1][0], lst[i][1][1]))
    elif sortcommand == 'mobile:False':
        lst = sorted(d.items(), key=lambda v: v[1][1], reverse=False)
        for i in range(len(lst)):
            print('{:^10}{:^10}{:^20}'.format(lst[i][0], lst[i][1][0], lst[i][1][1]))
    elif sortcommand == 'exit':  # 退出
        return
    else:
        print('sort command error:username:True')


import msvcrt
import shelve  #调用shelve函数
d = shelve.open("test")
p = shelve.open("password")
error = 'user data does not exist' #定义输入错误
#print('Please input the command：add|delete|update|find|list|exit')  #打印命令
if p == {}:
    print('first time running the system, please set the administrator password')
    passwd = getpass()
    print('Please enter your password again.')
    repasswd = getpass()
    while passwd != repasswd or passwd == '':
        print('Inconsistent passwords,set your password again.')
        continue
    else:
        p[passwd] = passwd
        print('Password Setting Successfully')
else:
    # print('Please enter the administrator password')
    password = getpass()
    password_judge(password)
while True:   #死循环
    if d == {}:  #判断是否为空，是否需要添加数据
        print('No data exists ,Please add data first:username:age:contact information')
    else:
        print('Please input the command：add|delete|update|find|list|exit')
    command = input('>>>') #输入命令
    if command == 'add':  #命令的判读
        password = getpass()
        password_judge(password)
        print('Please add data:username:age:contact information')  #数据格式
        data = input('>>>')  #数据添加
        data = input_data(data)
        add_data(data)
    elif command == 'delete': #数据删除
        password = getpass()
        password_judge(password)
        data = input('Please input the username')  #输入username
        delete_add(data)
    elif command == 'update':#跟新
        password = getpass()
        password_judge(password)
        data = input('Please input the username:age:contact information')
        data = input_data(data)
        update_data(data)
    elif command == 'find': #查找
        password = getpass()
        password_judge(password)
        data = input('Please input the username')
        find_data(data)
    elif command == 'list':  #列出来
        password = getpass()
        password_judge(password)
        list_data(command)
        sortcommand = input('sort command:>>>')#是否需要排序
        sort_data(sortcommand)
    elif command == 'exit': #退出
        print('Thank you for using,user data has been saved.')
        break
    else:
        print('Command input error') #命令输入错误的输出
