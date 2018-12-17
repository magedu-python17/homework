import shelve  #调用shelve函数
d = shelve.open("test")
error = 'user data does not exist' #定义输入错误
print('Please input the command：add|delete|update|find|list|exit')  #打印命令
while True:   #死循环
    if d == {}:  #判断是否为空，是否需要添加数据
        print('No data exists ,Please add data first:username:age:contact information')
    command = input('>>>') #输入命令
    if command == 'add':  #命令的判读
        print('Please add data:username:age:contact information')  #数据格式
        data = input('>>>')  #数据添加
        if data.count(":") == 2 and (data.split(':', 2)[0]) != '' and (data.split(':', 2)[1]).isdigit() and (data.split(':', 2)[2]).isdigit(): #判断数据是否符合格式
            data = data.split(':', 1) #拆分成两部分 。前一部分为username为key，后一部分年龄和联系方式为vaule
            if data[0] in d:   #判断keyz在不在d中，在d中就让跟新
                print('user data exist, please update')
            else:
                d[data[0]] = data[1]    #不在就添加进去
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
        if data.count(":") == 2 and (data.split(':', 2)[0]) != '' and (data.split(':', 2)[1]).isdigit() and (data.split(':', 2)[2]).isdigit():#判断格式
            data = (data.split(':', 1)) #输入数据并拆分成两部分
            if data[0] in d: #判断是否在d中
                d.update({data[0]: data[1]}) #在就跟新
                print('update success')
            else:
                print(error)  #不在就报错
        else:
            print('data in wrong format')
    elif command == 'find': #查找
        data = input('Please input the username')
        if data in d:   #判断是否在d中
            print('username    | age  |   contact information')
            print('{:^10}{:^10}{:^20}'.format(k, d[k].split(':')[0], d[k].split(':')[1])) #打印数据
        else:
            print(error)
    elif command == 'list':  #列出来
        print('username    | age  |   contact information')
        for k in d:
            print('{:^10}{:^10}{:^20}'.format(k, d[k].split(':')[0], d[k].split(':')[1])) #列出来
    elif command == 'exit': #退出
        print('Thank you for using,user data has been saved.')
        break
    else:
        print('Command input error') #命令输入错误的输出

# 和前面的那个一样的，想想哈