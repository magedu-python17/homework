# 第一周正式作业班主任-薇薇 12月10号 星期一 14:55
# 各位宝宝们开班后第一次作业布置，激不激动，大家要按时提交哦 本周作业内容如下（12.10-12.16）：
# 实现一个用户管理系统，可以与管理员用户进行交互(本次先不实现验证密码之类的)，根据用户输入的指令(增删改查)，可以进行相应的操作：
# 比如 1.输入delete，则让用户输入”用户名”格式字符串，根据用户名查找内存里面的数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在;
# 2.输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找内存中数据，若存在数据则将改数据更新数据，若用户数据不存在，
# 则提示不存在;
# 3. 用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找内存中数据包
# 含输入字符串的用户信息，并打印;
# 4.用户输入list，则打印所有用户信息;打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;
# 5.用户输入exit，则提示用户并且保存已经修改的用户信息，退出程序;
# 注意：首次运行时候或者用户为0的时候，需提示用户先添加数据。



UserName=['yang1','yang22','yang3','yang4']
UserAge=[15,16,17,18]
UserPhone=['18916775566','18916775567','18916775568','18916775569']
if len(UserName)==0:
    userinfo=input("Pleas add user info first,and use colons as separators")
    UserName.append(userinfo.split(':')[0])
    UserAge.append(userinfo.split(':')[1])
    UserPhone.append(userinfo.split(':')[2])
else:
    user_instructions=input("Please enter instructions\n")
    if user_instructions=='delete':
        username = input("Pleas input ausername you want to delete\n")
        if username in UserName:
            delete_num = UserName.index(username)
            del UserName[delete_num]
            del UserAge[delete_num]
            del UserPhone[delete_num]
            # print(UserName,UserAge,UserPhone)
        else:
            print("there is no user called",username)

    elif user_instructions=='find':
        username = input("Pleas input ausername you want to find\n")
        find_flag=UserName.count(username)
        if  username in UserName:
            find_num=UserName.index(username)
            print("USER INFO \nusername:{}age:{}phoneno{}".format(UserName[find_num],UserAge[find_num],UserPhone[find_num]))
        else:
            print("there is no user called", username)
    else:
        print("exit")
        exit()


# 正常的话一个系统，是有用户来选择是否退出的，而不是每次操作完自动结束的，还有add, list和 update的没有实现，再优化下



