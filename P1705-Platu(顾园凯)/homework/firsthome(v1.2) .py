import shelve  #调用shelve函数
d = shelve.open("test")
error = 'user data does not exist' #定义输入错误
#print('Please input the command：add|delete|update|find|list|exit')  #打印命令
while True:   #死循环
    if d == {}:  #判断是否为空，是否需要添加数据
        print('No data exists ,Please add data first:username:age:contact information')
    else:
        print('Please input the command：add|delete|update|find|list|exit')
    command = input('>>>') #输入命令
    if command == 'add':  #命令的判读
        print('Please add data:username:age:contact information')  #数据格式
        data = input('>>>')  #数据添加
        if data.count(":") == 2: #判断添加的数据的格式
            username, age, mobile = data.split(':', 2) #拆分成3部分 。前一部分为username为key，后两部分年龄和联系方式为age和mobile
            if username == '' or not age.isdigit() or not mobile.isdigit:   #判断username 和age ，mobile是否符合要求
                print('data in wrong format')#不符合就报错
            else:
                if username in d:#符合要求就判断数据是否存在
                    print('user data exist, please update')
                else:
                    d[username] = [age, mobile]    #不在就添加进去
                    print('add success')
        else:
            print('data in wrong format') #不符合就报错
    elif command == 'delete': #数据删除
        data = input('Please input the username')  #输入username
        if data in d: #判断username在不在key中
            del d[data]  #在就删除
            print('delete success')
        else:
            print(error) #不在就报错
    elif command == 'update':#跟新
        data = input('Please input the username:age:contact information')
        if data.count(":") == 2:#判断数据
            username, age, mobile = data.split(':', 2) #输入数据并拆分成三部分
            if username != 0 and age.isdigit() and mobile.isdigit:#判断三部分是否符合要求
                if username in d: #判断是否在d中
                    d.update({username: [age, mobile]}) #在就跟新
                    print('update success')
                else:
                    print(error)  #不在就报错
            else:
                print('data in wrong format')
        else:
            print('data in wrong format')
    elif command == 'find': #查找
        data = input('Please input the username')
        if data in d:   #判断是否在d中
            print('username    | age  |   mobile information')
            print('{:^10}{:^10}{:^20}'.format(data, d[data][0], d[data][1])) #打印数据
        else:
            print(error)
    elif command == 'list':  #列出来
        if d == {}:
            continue
        print('username    | age  |   mobile information')
        for k in d:
            print('{:^10}{:^10}{:^20}'.format(k, d[k][0], d[k][1])) #列出来
        print('if you want to sort,please input sort command:(username or age or mobile):resrver(Ture or False)\n''if you do not want sort please input exit')
        sortcommand = input('sort command:>>>')#是否需要排序
        if sortcommand != 'exit':#排序的话就打印数据标题
            print('username    | age  |   mobile information')
        if sortcommand == 'username:True':#排序命令
            lst = sorted(d.items(), reverse=True)
            for i in range(len(lst)):#排序打印
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
        elif sortcommand == 'exit':#退出
            continue
        else:
            print('sort command error:username:True')
    elif command == 'exit': #退出
        print('Thank you for using,user data has been saved.')
        break
    else:
        print('Command input error') #命令输入错误的输出
