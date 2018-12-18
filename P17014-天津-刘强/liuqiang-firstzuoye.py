import  pandas as pd
#首行用户描述信息
name = ['人名','年龄','联系方式']
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
            '输入exit:---完成提示用户并且保存已经修改的用户信息，退出程序操作;')
print("用户管理系统相关使用说明如下：")
for num1 in range(5):
    print(usetuple[num1])
print("----------------------------------------------------------------------------------------------")
#运行主程序段
while True:
    if flag1:
        break
    #每次运行系统，根据异常判断，是否存在该文件，不存在就创建
    #如果存在该文件，都读取本地文件内容到内存列表中
    #*.csv数据文件需要提前生成，只包含一行用户描述信息（名字,年龄，联系方式）
    try:
        source_data = pd.read_csv('D:/test9.csv', header=None, names=name, encoding='gb2312')
    except:
        file = pd.DataFrame(columns=name)
        file.to_csv('D:/test9.csv', index=False, encoding='gb2312')
        continue
    else:
            source_data = pd.read_csv('D:/test9.csv', header=None, names=name,encoding='gb2312')
            #将从文件读取的数据转换成列表
            data = source_data.values.tolist()
            # 取列表长度
            datalengthcount = len(data)
            # 登录系统，判断如果列表长度为1，则证明无任何用户数据信息，需要至少添加一行用户信息
            if datalengthcount == 1:
                print('当前管理系统没有任何用户数据，请添加一行新数据!')
                userstring = input('请输入格式(人名:年龄:联系方式)三个字段信息且以冒号分割字段:').strip().split(':')
                data.append(userstring)
                datalengthcount += 1 #从第二行开始，依次追加用户信息，长度计数增加
                while True:
                    if flag2 == True:
                        break
                    optionstring = input('是否还继续添加用户信息:yes or no:')
                    if optionstring == 'yes':
                        userstring = input('请输入格式(人名:年龄:联系方式)三个字段信息且以冒号分割字段:').strip().split(':')
                        data.append(userstring)
                        datalengthcount += 1
                    elif optionstring == 'no':
                        while True:
                            if flag3:
                                break
                            comstring = input('请输入任何一个指令完成相应操作：delete or update or find or list or insert or exit:').strip()
                            if comstring == 'delete':
                                username = input('请输入要删除的用户名:').strip()
                                if datalengthcount == 1:
                                    print('当前管理系统无任何用户数据信息！！！')
                                    break
                                for num3 in range(1,datalengthcount):
                                    if data[num3][0] == username:
                                        data.pop(num3)
                                        print('该用户相关数据信息已经删除！')
                                        datalengthcount -= 1 #每删除一行用户信息,列表长度递减
                                        break
                                else:
                                    print('要删除的用户不存在！！！')
                            elif comstring == 'update':
                                userline = input('请输入需要更新用户的数据行,格式(用户名:年龄:联系方式):').strip().split(':')
                                for num4 in range(1,datalengthcount):
                                    if data[num4][0] == userline[0]:
                                        for num5 in range(1,3):
                                            data[num4][num5] = userline[num5]
                                        print('该用户信息已经更新！')
                                        break
                                else:
                                    print('要更新的用户不存在！！！')
                            elif comstring == 'find':
                                findusername = input('请输入需要查找的用户名:').strip()
                                for num6 in range(1, datalengthcount):
                                    if data[num6][0] == findusername:
                                        print('用户数据信息:')
                                        for num7 in range(len(data[num6])):
                                            print('{:10}'.format(data[num6][num7]),end='')
                                        print()
                                        break
                                else:
                                    print('要查找的用户不存在！！！')
                            elif comstring == 'list':
                                print('管理系统所有用户数据信息如下:')
                                for num8 in range(0,3):
                                    print('{:18}'.format(data[0][num8]), end='')
                                print()
                                for num9 in range(1,datalengthcount):
                                    for num10 in range(0,3):
                                        print('{:20}'.format(data[num9][num10]),end='')
                                    print()
                            elif comstring == 'insert':
                                insertstring = input('请输入格式(人名:年龄:联系方式)三个字段信息且以冒号分割字段:').strip().split(':')
                                for num11 in range(1,datalengthcount):
                                    if data[num11][0] ==  insertstring[0]:
                                        print('该用户已经存在，请重新输入数据！！！')
                                        break
                                else:
                                    data.append(insertstring)
                                    print('用户数据插入完成！！！')
                                    datalengthcount += 1
                            # 保存内存数据到本地文件存储，并且跳出三层死循环结束整个程序
                            elif comstring == 'exit':
                                print("保存数据，退出管理系统！！！")
                                # 必须弹出首行用户描述信息，否则会出现首行重复情况
                                data.pop(0)
                                file = pd.DataFrame(columns=name, data=data)
                                file.to_csv('D:/test9.csv', index=False, encoding='gb2312')
                                flag1 = True
                                flag2 = True
                                flag3 = True
                                break
                            else:
                                print('输入的指令不正确，请重新输入:')
                    else:
                        print('"yes or no"不正确，请重新输入:')
                        continue
            # 登录系统，数据库存在相关用户数据信息的情况，即列表长度至少为2
            else:
                while True:
                    if flag4:
                        break
                    comstring = input('请输入任何一个指令完成相应操作：delete or update or find or list or insert or exit:').strip()
                    if comstring == 'delete':
                        username = input('请输入要删除的用户名:').strip()
                        if datalengthcount == 1:
                            print('当前管理系统无任何用户数据信息，请重新输入指令操作！！！')
                            continue
                        for num3 in range(1, datalengthcount):
                            if data[num3][0] == username:
                                data.pop(num3)
                                print('该用户相关数据信息已经删除！')
                                datalengthcount -= 1  # 每删除一行用户信息,列表长度递减
                                break
                        else:
                            print('要删除的用户不存在！！！')
                    elif comstring == 'update':
                        userline = input('请输入需要更新用户的数据行,格式(用户名:年龄:联系方式):').strip().split(':')
                        for num4 in range(1, datalengthcount):
                            if data[num4][0] == userline[0]:
                                for num5 in range(1, 3):
                                    data[num4][num5] = userline[num5]
                                print('该用户信息已经更新！')
                                break
                        else:
                            print('要更新的用户不存在！！！')
                    elif comstring == 'find':
                        findusername = input('请输入需要查找的用户名:').strip()
                        for num6 in range(1, datalengthcount):
                            if data[num6][0] == findusername:
                                print('用户数据信息:')
                                for num7 in range(len(data[num6])):
                                    print('{:10}'.format(data[num6][num7]), end='')
                                print()
                                break
                        else:
                            print('要查找的用户不存在！！！')
                    elif comstring == 'list':
                        print('管理系统所有用户数据信息如下:')
                        for num8 in range(0, 3):
                            print('{:18}'.format(data[0][num8]), end='')
                        print()
                        for num9 in range(1, datalengthcount):
                            for num10 in range(0, 3):
                                print('{:20}'.format(data[num9][num10]), end='')
                            print()
                    elif comstring == 'insert':
                        insertstring = input('请输入格式(人名:年龄:联系方式)三个字段信息且以冒号分割字段:').strip().split(':')
                        for num11 in range(1, datalengthcount):
                            if data[num11][0] == insertstring[0]:
                                print('该用户已经存在，请重新输入数据！！！')
                                break
                        else:
                            data.append(insertstring)
                            print('用户数据插入完成！！！')
                            datalengthcount += 1
                    # 保存内存数据到本地文件存储，并且跳出三层死循环结束整个程序
                    elif comstring == 'exit':
                        print("保存数据，退出管理系统！！！")
                        # 必须弹出首行用户描述信息，否则会出现首行重复情况
                        data.pop(0)
                        file = pd.DataFrame(columns=name, data=data)
                        file.to_csv('D:/test9.csv', index=False, encoding='gb2312')
                        flag1 = True
                        flag4 = True
                        break
                    else:
                        print('输入的指令不正确，请重新输入:')











