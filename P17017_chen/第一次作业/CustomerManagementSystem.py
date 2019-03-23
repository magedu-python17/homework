def fun():  # 帮助提示函数
    print("欢迎光临用户管理系统")
    print(" 1.update")
    print(" 2.delete")
    print(" 3.find")
    print(" 4.list")
    print(" 5.exit")


test_user = []  # 定义列表，存储数据


def ver_save():  # 保存数据，将数据保存到文件中
    SaveFile = open('testfile', 'w+')
    for n in test_user:
        SaveFile.write(str(n))
    SaveFile.close()


def ver_update(x=0, flag=0):  # 新增数据函数
    userId = input('请输入用户id：')
    username = input('请输入用户姓名：')
    age = input('请输入用户年龄：')
    contact = input('请输入联系方式：')
    print("您输入的信息为:{}:{}:{}:{}".format(userId, username, age, contact))
    for i in test_user:
        if i['id'] == userId:
            flag = 1
            break
        else:
            x += 1
    if flag == 1:
        print('用户id已存在')
    else:
        user = {'id': userId, 'name': username, 'age': age, 'contact': contact}  # 定义存放单个用户的字典
        test_user.append(user)  # 将存放单个用户的字典追加到test_user列表中
        ver_save()


def ver_delete(x=0, flag=0):  # 删除数据
    delid = input('请输入用户id：')
    for i in test_user:
        if i['id'] == delid:
            flag = 1
            break
        else:
            x += 1
    if flag == 0:
        print("没有此用户，请添加用户！")
    else:
        del test_user[x]  # 删除test_user列表中索引为x的元素
        ver_save()


def ver_find(x=0, flag=0):  # 查找数据
    SearchID = input('请输入要查找的用户id：')
    for i in test_user:
        if i['id'] == SearchID:
            flag = 1
            break
        else:
            x += 1
    if flag == 0:
        print('没有此用户，请添加用户！')
    else:
        print('查询结果：')
    print("id:{} name:{} age:{} contact:{}".format(i['id'], i['name'], i['age'], i['contact']))


def ver_list():  # 格式化展示
    print('id   name   age   contact')
    for i in test_user:
        if i:
            print("{}   {}   {}   {}".format(i['id'], i['name'], i['age'], i['contact']))
        else:
            print('没有用户，请添加用户！')


def ver_exit():  # 退出系统
    print('退出系统')


while True:
    fun()  # 调用fun函数
    Var = input("请输入选择的功能：")
    if Var == 'update':
        ver_update()
    elif Var == 'delete':
        ver_delete()
    elif Var == 'find':
        ver_find()
    elif Var == 'list':
        ver_list()
    elif Var == 'exit':
        ver_exit()
        break
    else:
        print('请确认输入是否正确！')

# 少个当用户为0的时候，提示管理员添加用户, 还有update的时候，你是以name为主键的，这里是有问题的，你试试name相同情况下，别的没有啥，再优化下