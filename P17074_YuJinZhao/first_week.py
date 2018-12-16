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
Uname = []
Uage = []
Ucontact = []  # 用户的三个信息分别建个列表
user_counts = 0  # 这个用来方便打印insert信息,及统计用户总数
user_id = 0
if Uname == []:  # 如果列表里没有数据，让用户输入信息并分别追加到列表
    while True:
        print("Please add data>>>")
        Uname.append(input('UserName:'))
        Uage.append(input('UserAge:'))
        Ucontact.append(input('UserContact:'))
        print('A data insert>> {}:{}:{}'.format(Uname[user_counts], Uage[user_counts], Ucontact[user_counts]))
        user_counts += 1
        choice = input('continue insert? (y/n)')  # 如果用户输入Y，则继续插入下个用户信息,否则退出
        if choice == 'y':
            pass
        else:
            break
# 列表有数据后提示用户键入命令
print('start your service>>>')

while True:
    print('options: delete/update/find/list/exit')
    command = input('cmd# ')
# ________________________
    if command == 'delete':
        print('enter the user you want to delete>>>')
        tmp_ = input('delete# ')  # 临时变量存着用户要删除的用户
        if tmp_ in Uname:  # 如果用户输入的名字在列表，则依次删除用户信息,用户数-1
            tmp_id = Uname.index(tmp_)
            del Uname[tmp_id]
            del Uage[tmp_id]
            del Ucontact[tmp_id]
            user_counts -= 1
        else:
            print('user not exist')


    if command == 'update':
        print('enter this format: username:age:contact  >>>')
        tmp_ = input('update# ')
        tmp_name = tmp_.split(':')[0]  # 取出用户名看其是否存在，若存在，更新另外两项
        if tmp_name in Uname:
            tmp_id = Uname.index(tmp_name)
            Uage[tmp_id] = tmp_.split(':')[1]
            Ucontact[tmp_id] = tmp_.split(':')[2]
            print('user updated successfully')
        else:
            print('user not exist ')


    if command == 'find':  # 同上
        print('input a user name>>>')
        tmp_ = input('find# ')
        if tmp_ in Uname:
            tmp_id = Uname.index(tmp_)
            print('{}:{}:{}'.format(Uname[tmp_id], Uage[tmp_id], Ucontact[tmp_id]))
        else:
            print('no such user')


    if command == 'list':
        print('__{} {:>5} {:>10}__'.format('user', 'age', 'contact'))
        lst_len = len(Uname)  # 列表的长度即用户总数
        for i in range(lst_len): # 做循环依次打印几个列表的数据
            print('  {} {:>5} {:>10}'.format(Uname[i], Uage[i], Ucontact[i]))

    if command == 'exit':
        break
