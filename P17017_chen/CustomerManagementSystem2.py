'''
简单的用户信息管理系统
'''


def help():
    print('---欢迎进入用户信息管理系统---\n可以进行如下操作：\nadd:新增用户信息\nupdate:修改用户信息\n'
          'delete:删除用户信息\nfind:查找用户信息\nlist:打印用户列表\nsort:排序\nexit:退出系统\n=====================')


user_Dict = {}  # 定义一个空字典


def ver_save():  # 保存数据，将数据保存到文件中
    with open('testfile', 'w+') as f:
        f.write(str(user_Dict))


def ver_register(username, password):  # 注册用户
    temp = username + '|' + password
    with open('user_passwd', 'w')as f:  # 将注册的用户写入到文件中
        f.write(temp)


def ver_login(username, password):  # 用户登录
    f = open('user_passwd', 'r')  # 读文件
    list1 = f.read().split('|')
    if username == list1[0] and password == list1[1]:  # 验证用户名和密码
        print('登陆成功')
        return True
    else:
        print('登陆失败')
        return False


def ver_add(flag=0):  # 新增用户
    userid = input('请输入用户id：')
    username = input('请输入用户姓名：')
    age = input('请输入用户年龄：')
    tel = input('请输入用户联系方式：')
    print('你输入的信息为id:{} name:{} age:{} tel:{}'.format(userid, username, age, tel))
    for k, v in user_Dict.items():
        if int(k) > flag:
            flag = int(k)
        if k[0] == userid:
            print('请不要输入已存在的id')
    flag += 1  # 循环一次flag自增1，
    user = {'id': userid, 'name': username, 'age': age, 'tel': tel}
    user_Dict[str(flag)] = user  # 将flag定义为字典的key值，将user赋值给key
    ver_save()  # 将字典信息保存到文件中


def ver_delete():  # 跟你用户id删除用户
    UserID = input('请输入你要删除的用户id：')
    for k, v in list(user_Dict.items()):  # 遍历字典
        if v['id'] == UserID:  # 如果输入的id等于Values中的id
            del user_Dict[k]  # 删除key为k的元素
            ver_save()  # 保存删除后的数据
        else:
            print('请输入正确UserID')


def ver_list():  # 格式化输出
    print('{}   {:>10}   {:>10}   {:>10}'.format('id', 'name', 'age', 'tel'))
    for v in user_Dict.values():
        if v:
            print("{}   {:>10}   {:>10}   {:>10}".format(v['id'], v['name'], v['age'], v['tel']))
        else:
            print('没有用户，请添加用户！')


def ver_find():  # 根据用户id查找用户
    UserID = input('请输入你要查询的用户id：')
    for v in user_Dict.values():
        if v['id'] == UserID:
            print(v)
        else:
            print('请输入正确的id')


def ver_sort():  # 按用户时输入字段排序，返回二元组
    ret = input('请输入要进行排序的字段')
    if ret == '':
        print(sorted(user_Dict.items(), key=lambda item: item[1]['name']))
    elif ret == 'id':
        print(sorted(user_Dict.items(), key=lambda item: item[1]['id']))
    elif ret == 'age':
        print(sorted(user_Dict.items(), key=lambda item: item[1]['age']))


def ver_exit():  # 退出系统
    print('退出系统')

help()
while True:
    ver = input('请输入操作命令：')
    if ver == 'register':
        username = input('请输入用户名：')
        password = input('请输入密码：')
        ver_register(username, password)
    elif ver == 'add':
        username = input('请进行用户名验证：')
        password = input('请进行密码验证：')
        res = ver_login(username, password)
        if res:
            ver_add()
        else:
            print('请输入正确的用户名和密码')
    elif ver == 'delete':
        username = input('请进行用户名验证：')
        password = input('请进行密码验证：')
        res = ver_login(username, password)
        if res:
            ver_delete()
        else:
            print('请输入正确的用户名和密码')
    elif ver == 'list':
        username = input('请进行用户名验证：')
        password = input('请进行密码验证：')
        res = ver_login(username, password)
        if res:
            ver_list()
        else:
            print('请输入正确的用户名和密码')
    elif ver == 'find':
        username = input('请进行用户名验证：')
        password = input('请进行密码验证：')
        res = ver_login(username, password)
        if res:
            ver_find()
        else:
            print('请输入正确的用户名和密码')
    elif ver == 'sort':
        username = input('请进行用户名验证：')
        password = input('请进行密码验证：')
        res = ver_login(username, password)
        if res:
            ver_sort()
        else:
            print('请输入正确的用户名和密码')
    elif ver == 'exit':
        ver_exit()
        break

