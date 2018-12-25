import pandas as pd
from operator import itemgetter
#首行用户描述信息
name = ['name','age','telephone']
#首行账户名称和密码
confirmpass = ['account','password']
#跳出各层死循环的开关标记
#主程序段最外层死循环开关
flag1 = False
#数据库没有任何用户数据信息时，用于跳出条件分支的死循环开关
flag2 = False
flag3 = False
#数据库有用户相关数据信息时，用于跳出条件分支的死循环开关
flag4 = False
#系统使用说明
usetuple = ('输入delete:"用户名"---完成删除用户信息操作',\
            '输入update:"用户名:年龄:联系方式"---完成更新数据操作',\
            '输入find:"用户名"---完成查找用户信息操作',\
            '输入list:---完成打印所有用户信息操作(第一行为用户描述细信息，第二行为用户数据信息)',\
            '输入insert:---完成插入用户信息操作，格式为（用户名:年龄:联系方式）',\
            '输入exit:---完成提示用户并且保存已经修改的用户信息，退出程序操作',\
            '输入resetpass:---重置管理员名称和密码',\
            '输入sortdata:---完成系统数据升序或降序排序（按照name,age,telephone排序），默认以name字段排序')
print("用户管理系统相关使用说明如下：")
for num1 in range(7):
    print(usetuple[num1])
print("----------------------------------------------------------------------------------------------")
#运行主程序段
while True:
    if flag1:
        break
    #每次运行系统，根据异常判断，是否存在该文件，不存在就创建
    #如果存在该文件，都读取本地文件内容到内存列表中
    #*.csv数据文件需要提前生成，只包含一行用户描述信息（名字,年龄，联系方式）
    #dtype={'age':int,'telephone':int}
    try:
        source_data = pd.read_csv('D:/test9.csv',encoding='gb2312',names=name)
        source_data1 = pd.read_csv('D:/test8.csv',encoding='gb2312',names=confirmpass)
    except:
        #创建数据文件，加上列名，并且去掉索引
        file = pd.DataFrame(columns=name)
        file.to_csv('D:/test9.csv', index=False, encoding='gb2312')
        #创建管理员和密码文件
        file1 = pd.DataFrame(columns=confirmpass)
        file1.to_csv('D:/test8.csv', index=False, encoding='gb2312')
        continue
    else:
            #将从文件读取的数据转换成列表
            data = source_data.values.tolist()
            #取列表长度
            datalengthcount = len(data)
            #登录系统，判断如果列表长度为1，则证明无任何用户数据信息，需要至少添加一行用户信息
            if datalengthcount == 1:
                print('首次登录用户管理系统!')
                data1 = source_data1.values.tolist()
                # 将列表转成元组
                data2 = (data1[0][0], data1[0][1])
                # 初始化一个字典，用于存放用户名和密码（格式:{'account':'admin','password':'123'}）
                passwd = {}
                passstring = input('请设置(account:password)管理员账户名称和密码,这两个字段信息且以冒号分割字段:').strip().split(':')
                #设置的账户名称和密码赋予内存字典
                for pas in range(len(passstring)):
                    passwd[data2[pas]] = passstring[pas]
                print('当前管理系统没有任何用户数据，请添加一行新数据!')
                userstring = input('请输入格式(name:age:telephone)三个字段信息且以冒号分割字段:').strip().split(':')
                #将age和tel字段转换成整数，以便后续进行排序
                for tag in range(1,3):
                    userstring[tag] = int(userstring[tag])
                data.append(userstring)
                datalengthcount += 1 #从第二行开始，依次追加用户信息，长度计数增加
                while True:
                    if flag2 == True:
                        break
                    optionstring = input('是否还继续添加用户信息:yes or no:')
                    if optionstring == 'yes':
                        userstring = input('请输入格式(name:age:telephone)三个字段信息且以冒号分割字段:').strip().split(':')
                        for tag in range(1, 3):
                            userstring[tag] = int(userstring[tag])
                        data.append(userstring)
                        datalengthcount += 1
                    elif optionstring == 'no':
                        while True:
                            if flag3:
                                break
                            comstring = input('请输入任何一个指令完成相应操作：delete or update or find or list or insert or exit or resetpass or sortdata:').strip()
                            if comstring == 'delete':
                                # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                                lstpasswd = []
                                print('请输入管路员名称和密码进行验证!')
                                lstpasswd.append(input('请输入管理员账户名称===>'))
                                lstpasswd.append(input('请输入管理密码===>'))
                                if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                                    print('验证成功!')
                                else:
                                    print('输入的账户名称或密码错误，请重新选择指令，进入验证模式!')
                                    continue
                                username = input('请输入要删除的用户名:').strip()
                                if datalengthcount == 1:
                                    print('当前管理系统无任何用户数据信息！！！')
                                    break
                                for num3 in range(1,datalengthcount):
                                    if data[num3][0] == username:
                                        data.pop(num3)
                                        print('该用户相关数据信息已经删除!')
                                        datalengthcount -= 1 #每删除一行用户信息,列表长度递减
                                        break
                                else:
                                    print('要删除的用户不存在!!!')
                            elif comstring == 'update':
                                # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                                lstpasswd = []
                                print('请输入管路员名称和密码进行验证!')
                                lstpasswd.append(input('请输入管理员账户名称===>'))
                                lstpasswd.append(input('请输入管理密码===>'))
                                if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                                    print('验证成功!')
                                else:
                                    print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                                    continue
                                userline = input('请输入需要更新用户的数据行,格式(name:age:telephone):').strip().split(':')
                                for num4 in range(1,datalengthcount):
                                    if data[num4][0] == userline[0]:
                                        for num5 in range(1,3):
                                            data[num4][num5] = userline[num5]
                                        print('该用户信息已经更新!')
                                        break
                                else:
                                    print('要更新的用户不存在!!!')
                            elif comstring == 'find':
                                # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                                lstpasswd = []
                                print('请输入管路员名称和密码进行验证!')
                                lstpasswd.append(input('请输入管理员账户名称===>'))
                                lstpasswd.append(input('请输入管理密码===>'))
                                if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                                    print('验证成功!')
                                else:
                                    print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                                    continue
                                findusername = input('请输入需要查找的用户名:').strip()
                                for num6 in range(1, datalengthcount):
                                    if data[num6][0] == findusername:
                                        print('用户数据信息:')
                                        for num7 in range(len(data[num6])):
                                            print('{:<8}'.format(data[num6][num7]),end='')
                                        print()
                                        break
                                else:
                                    print('要查找的用户不存在!!!')
                            elif comstring == 'list':
                                # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                                lstpasswd = []
                                print('请输入管路员名称和密码进行验证!')
                                lstpasswd.append(input('请输入管理员账户名称===>'))
                                lstpasswd.append(input('请输入管理密码===>'))
                                if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                                    print('验证成功!')
                                else:
                                    print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                                    continue
                                print('管理系统所有用户数据信息如下:')
                                for num8 in range(0,3):
                                    print('{:<8}'.format(data[0][num8]), end='')
                                print()
                                for num9 in range(1,datalengthcount):
                                    for num10 in range(0,3):
                                        print('{:<8}'.format(data[num9][num10]),end='')
                                    print()
                            elif comstring == 'insert':
                                # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                                lstpasswd = []
                                print('请输入管路员名称和密码进行验证!')
                                lstpasswd.append(input('请输入管理员账户名称===>'))
                                lstpasswd.append(input('请输入管理密码===>'))
                                if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                                    print('验证成功!')
                                else:
                                    print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                                    continue
                                insertstring = input('请输入格式(name:age:telephone)三个字段信息且以冒号分割字段:').strip().split(':')
                                for num11 in range(1,datalengthcount):
                                    if data[num11][0] ==  insertstring[0]:
                                        print('该用户已经存在，请重新输入数据!!!')
                                        break
                                else:
                                    for tag in range(1, 3):
                                        insertstring[tag] = int(insertstring[tag])
                                    data.append(insertstring)
                                    print('用户数据插入完成!!!')
                                    datalengthcount += 1
                            # 保存内存用户信息数据到本地文件存储，并且跳出三层死循环结束整个程序
                            elif comstring == 'exit':
                                print("保存数据，退出管理系统!!!")
                                file = pd.DataFrame(data=data)
                                #写入文件时，去掉内存中列表的第一行数据，也就是用户描述信息
                                file.to_csv('D:/test9.csv',header=0,encoding='gb2312',index=False)
                                #保存管理员账户和密码信息数据写入文件
                                #需要先转换成列表 在存入文件中
                                passlst = [passwd]
                                file1 = pd.DataFrame(passlst)
                                file1.to_csv('D:/test8.csv', index=False, encoding='gb2312')
                                flag1 = True
                                flag2 = True
                                flag3 = True
                                break
                            elif comstring == 'resetpass':
                                passstring = input('请重新输入(格式account:password)管理员账户名称和密码,这两个字段信息且以冒号分割字段:').strip().split(':')
                                # 覆盖现有字典中保存的管理员名称和密码
                                #定义临时变量遍历重新输入的account和password 覆盖字典原有数据
                                tmp = 0
                                for pas in passwd.keys():
                                    passwd[pas] = passstring[tmp]
                                    tmp += 1
                                print('管理账户和密码已经重置!请选择相应指令完成操作!!!')
                            elif comstring == 'sortdata':
                                sortstring = input('please input your sort algorithm:A(升序) or D(降序)==>')
                                sortstr = input('please choice your sort field:yes or no==>')
                                # 升序排序
                                if sortstring == 'A':
                                    # 默认以name ASCII码排序
                                    if sortstr == 'no':
                                        data.pop(0)
                                        data.sort(key=lambda x: x[0])
                                        print('排序后数据如下:')
                                        data.insert(0, name)
                                        for num8 in range(0, 3):
                                            print('{:<8}'.format(data[0][num8]), end='')
                                        print()
                                        for num9 in range(1, datalengthcount):
                                            for num10 in range(0, 3):
                                                print('{:<8}'.format(data[num9][num10]), end='')
                                            print()
                                    elif sortstr == 'yes':
                                        sortfield = input('please choice your sort field:age or tel==>')
                                        # 选择age字段排序 实际以数字大小排序
                                        if sortfield == 'age':
                                            data.pop(0)
                                            data.sort(key=itemgetter(1))
                                            print('排序后数据如下:')
                                            data.insert(0, name)
                                            for num8 in range(0, 3):
                                                print('{:<8}'.format(data[0][num8]), end='')
                                            print()
                                            for num9 in range(1, datalengthcount):
                                                for num10 in range(0, 3):
                                                    print('{:<8}'.format(data[num9][num10]), end='')
                                                print()
                                        # 选择tel字段排序 实际以数字大小排序
                                        elif sortfield == 'tel':
                                            data.pop(0)
                                            data.sort(key=itemgetter(2))
                                            print('排序后数据如下:')
                                            data.insert(0, name)
                                            for num8 in range(0, 3):
                                                print('{:<8}'.format(data[0][num8]), end='')
                                            print()
                                            for num9 in range(1, datalengthcount):
                                                for num10 in range(0, 3):
                                                    print('{:<8}'.format(data[num9][num10]), end='')
                                                print()
                                        else:
                                            print('输入的参数错误，请重新选择sortdata，选择相应的field进行排序!!!')
                                    else:
                                        print('输入的参数错误，请重新选择sortdata，重新输入yes or no!!!')
                                # 降序排序
                                elif sortstring == 'D':
                                    if sortstr == 'no':
                                        data.pop(0)
                                        data.sort(key=lambda x: x[0], reverse=True)
                                        print('排序后数据如下:')
                                        data.insert(0, name)
                                        for num8 in range(0, 3):
                                            print('{:<8}'.format(data[0][num8]), end='')
                                        print()
                                        for num9 in range(1, datalengthcount):
                                            for num10 in range(0, 3):
                                                print('{:<8}'.format(data[num9][num10]), end='')
                                            print()
                                    elif sortstr == 'yes':
                                        sortfield = input('please choice your sort field:age or tel==>')
                                        if sortfield == 'age':
                                            data.pop(0)
                                            data.sort(key=itemgetter(1), reverse=True)
                                            print('排序后数据如下:')
                                            data.insert(0, name)
                                            for num8 in range(0, 3):
                                                print('{:<8}'.format(data[0][num8]), end='')
                                            print()
                                            for num9 in range(1, datalengthcount):
                                                for num10 in range(0, 3):
                                                    print('{:<8}'.format(data[num9][num10]), end='')
                                                print()
                                        elif sortfield == 'tel':
                                            data.pop(0)
                                            data.sort(key=itemgetter(2), reverse=True)
                                            print('排序后数据如下:')
                                            data.insert(0, name)
                                            for num8 in range(0, 3):
                                                print('{:<8}'.format(data[0][num8]), end='')
                                            print()
                                            for num9 in range(1, datalengthcount):
                                                for num10 in range(0, 3):
                                                    print('{:<8}'.format(data[num9][num10]), end='')
                                                print()
                                        else:
                                            print('输入的参数错误，请重新选择sortdata，选择相应的field进行排序!!!')
                                    else:
                                        print('输入的参数错误，请重新选择sortdata，重新输入yes or no!!!')
                                else:
                                    print('输入的参数错误，请选择sortdata，选择A或者D进行排序!!!')
                            else:
                                print('输入的指令不正确，请重新输入:')
                    else:
                        print('"yes or no"不正确，请重新输入:')
                        continue
            #登录系统，数据库存在相关用户数据信息的情况，即列表长度至少为2
            else:
                #非首次登录系统，读取本地管理员密码信息到内存字典中
                data3 = source_data1.values.tolist()
                data4 = (data3[0][0], data3[0][1])
                data5 = (data3[1][0], data3[1][1])
                #初始化一个空字典，用来存储文件中的管理员名称和密码
                passwd = {}
                #将管理员账号和密码赋给内存字典
                for passnum in range(len(data3)):
                    passwd[data4[passnum]] = data5[passnum]
                #再次从文件读取的数据时字符串型，把age和tel字段转换成整数
                for intnum in range(1,datalengthcount):
                    for selnum in range(1,3):
                        data[intnum][selnum] = int(data[intnum][selnum])
                while True:
                    if flag4:
                        break
                    comstring = input('请输入任何一个指令完成相应操作：delete or update or find or list or insert or exit or resetpass or sortdata:').strip()
                    if comstring == 'delete':
                        # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                        lstpasswd = []
                        print('请输入管路员名称和密码进行验证!')
                        lstpasswd.append(input('请输入管理员账户名称===>'))
                        lstpasswd.append(input('请输入管理密码===>'))
                        if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                            print('验证成功!')
                        else:
                            print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                            continue
                        username = input('请输入要删除的用户名:').strip()
                        if datalengthcount == 1:
                            print('当前管理系统无任何用户数据信息，请重新输入指令操作!!!')
                            continue
                        for num3 in range(1, datalengthcount):
                            if data[num3][0] == username:
                                data.pop(num3)
                                print('该用户相关数据信息已经删除!')
                                datalengthcount -= 1  # 每删除一行用户信息,列表长度递减
                                break
                        else:
                            print('要删除的用户不存在!!!')
                    elif comstring == 'update':
                        # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                        lstpasswd = []
                        print('请输入管路员名称和密码进行验证!')
                        lstpasswd.append(input('请输入管理员账户名称===>'))
                        lstpasswd.append(input('请输入管理密码===>'))
                        if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                            print('验证成功!')
                        else:
                            print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                            continue
                        userline = input('请输入需要更新用户的数据行,格式(name:age:telephone):').strip().split(':')
                        for num4 in range(1, datalengthcount):
                            if data[num4][0] == userline[0]:
                                for num5 in range(1, 3):
                                    data[num4][num5] = userline[num5]
                                print('该用户信息已经更新!')
                                break
                        else:
                            print('要更新的用户不存在!!!')
                    elif comstring == 'find':
                        # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                        lstpasswd = []
                        print('请输入管路员名称和密码进行验证!')
                        lstpasswd.append(input('请输入管理员账户名称===>'))
                        lstpasswd.append(input('请输入管理密码===>'))
                        if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                            print('验证成功!')
                        else:
                            print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                            continue
                        findusername = input('请输入需要查找的用户名:').strip()
                        for num6 in range(1, datalengthcount):
                            if data[num6][0] == findusername:
                                print('用户数据信息:')
                                for num7 in range(len(data[num6])):
                                    print('{:<8}'.format(data[num6][num7]), end='')
                                print()
                                break
                        else:
                            print('要查找的用户不存在!!!')
                    elif comstring == 'list':
                        # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                        lstpasswd = []
                        print('请输入管路员名称和密码进行验证!')
                        lstpasswd.append(input('请输入管理员账户名称===>'))
                        lstpasswd.append(input('请输入管理密码===>'))
                        if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                            print('验证成功!')
                        else:
                            print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                            continue
                        print('管理系统所有用户数据信息如下:')
                        for num8 in range(0, 3):
                            print('{:<8}'.format(data[0][num8]), end='')
                        print()
                        for num9 in range(1, datalengthcount):
                            for num10 in range(0, 3):
                                print('{:<8}'.format(data[num9][num10]), end='')
                            print()
                    elif comstring == 'insert':
                        # 定义临时空列表,用于接收输入的管理员名称和密码,再与内存字典进行校验
                        lstpasswd = []
                        print('请输入管路员名称和密码进行验证!')
                        lstpasswd.append(input('请输入管理员账户名称===>'))
                        lstpasswd.append(input('请输入管理密码===>'))
                        if lstpasswd[0] == passwd.get('account') and lstpasswd[1] == passwd.get('password'):
                            print('验证成功!')
                        else:
                            print('输入账户名称或密码错误，请重新选择指令，进入验证模式!')
                            continue
                        insertstring = input('请输入格式(name:age:telephone)三个字段信息且以冒号分割字段:').strip().split(':')
                        for num11 in range(1, datalengthcount):
                            if data[num11][0] == insertstring[0]:
                                print('该用户已经存在，请重新输入数据!!!')
                                break
                        else:
                            for tag in range(1, 3):
                                insertstring[tag] = int(insertstring[tag])
                            data.append(insertstring)
                            datalengthcount += 1
                    # 保存内存数据到本地文件存储，并且跳出三层死循环结束整个程序
                    elif comstring == 'exit':
                        print("保存数据，退出管理系统!!!")
                        file = pd.DataFrame(data=data)
                        file.to_csv('D:/test9.csv', index=False,header=False,encoding='gb2312')
                        #保存管理员账户和密码信息数据写入文件
                        #需要先转换成列表 在存入文件中
                        passlst = [passwd]
                        file1 = pd.DataFrame(passlst)
                        file1.to_csv('D:/test8.csv', index=False, encoding='gb2312')
                        flag1 = True
                        flag4 = True
                        break
                    elif comstring == 'resetpass':
                        passstring = input('请重新输入(格式account:password)管理员账户名称和密码,这两个字段信息且以冒号分割字段:').strip().split(':')
                        # 覆盖现有字典中保存的管理员名称和密码
                        # 定义临时变量遍历重新输入的account和password 覆盖字典原有数据
                        tmp = 0
                        for pas in passwd.keys():
                            passwd[pas] = passstring[tmp]
                            tmp += 1
                        print('管理账户和密码已经重置!请选择相应指令完成操作!!!')
                    elif comstring == 'sortdata':
                        sortstring = input('please input your sort algorithm:A(升序) or D(降序)==>')
                        sortstr = input('please choice your sort field:yes or no==>')
                        #升序排序
                        if sortstring == 'A':
                            #默认以name ASCII码排序
                            if sortstr == 'no':
                                data.pop(0)
                                data.sort(key=lambda x:x[0])
                                print('排序后数据如下:')
                                data.insert(0,name)
                                for num8 in range(0, 3):
                                    print('{:<8}'.format(data[0][num8]), end='')
                                print()
                                for num9 in range(1, datalengthcount):
                                    for num10 in range(0, 3):
                                        print('{:<8}'.format(data[num9][num10]), end='')
                                    print()
                            elif sortstr == 'yes':
                                sortfield = input('please choice your sort field:age or tel==>')
                                #选择age字段排序 实际以数字大小排序
                                if sortfield == 'age':
                                    data.pop(0)
                                    data.sort(key=itemgetter(1))
                                    print('排序后数据如下:')
                                    data.insert(0, name)
                                    for num8 in range(0, 3):
                                        print('{:<8}'.format(data[0][num8]), end='')
                                    print()
                                    for num9 in range(1, datalengthcount):
                                        for num10 in range(0, 3):
                                            print('{:<8}'.format(data[num9][num10]), end='')
                                        print()
                                # 选择tel字段排序 实际以数字大小排序
                                elif sortfield == 'tel':
                                    data.pop(0)
                                    data.sort(key=itemgetter(2))
                                    print('排序后数据如下:')
                                    data.insert(0, name)
                                    for num8 in range(0, 3):
                                        print('{:<8}'.format(data[0][num8]), end='')
                                    print()
                                    for num9 in range(1, datalengthcount):
                                        for num10 in range(0, 3):
                                            print('{:<8}'.format(data[num9][num10]), end='')
                                        print()
                                else:
                                    print('输入的参数错误，请重新选择sortdata，选择相应的field进行排序!!!')
                            else:
                                print('输入的参数错误，请重新选择sortdata，重新输入yes or no!!!')
                        #降序排序
                        elif sortstring == 'D':
                            if sortstr == 'no':
                                data.pop(0)
                                data.sort(key=lambda x: x[0],reverse=True)
                                print('排序后数据如下:')
                                data.insert(0, name)
                                for num8 in range(0, 3):
                                    print('{:<8}'.format(data[0][num8]), end='')
                                print()
                                for num9 in range(1, datalengthcount):
                                    for num10 in range(0, 3):
                                        print('{:<8}'.format(data[num9][num10]), end='')
                                    print()
                            elif sortstr == 'yes':
                                sortfield = input('please choice your sort field:age or tel==>')
                                if sortfield == 'age':
                                    data.pop(0)
                                    data.sort(key=itemgetter(1), reverse=True)
                                    print('排序后数据如下:')
                                    data.insert(0, name)
                                    for num8 in range(0, 3):
                                        print('{:<8}'.format(data[0][num8]), end='')
                                    print()
                                    for num9 in range(1, datalengthcount):
                                        for num10 in range(0, 3):
                                            print('{:<8}'.format(data[num9][num10]), end='')
                                        print()
                                elif sortfield == 'tel':
                                    data.pop(0)
                                    data.sort(key=itemgetter(2), reverse=True)
                                    print('排序后数据如下:')
                                    data.insert(0, name)
                                    for num8 in range(0, 3):
                                        print('{:<8}'.format(data[0][num8]), end='')
                                    print()
                                    for num9 in range(1, datalengthcount):
                                        for num10 in range(0, 3):
                                            print('{:<8}'.format(data[num9][num10]), end='')
                                        print()
                                else:
                                    print('输入的参数错误，请重新选择sortdata，选择相应的field进行排序!!!')
                            else:
                                print('输入的参数错误，请重新选择sortdata，重新输入yes or no!!!')
                        else:
                            print('输入的参数错误，请选择sortdata，选择A或者D进行排序!!!')
                    else:
                        print('输入的指令不正确，请重新输入:')
