import msvcrt,sys
from dbconn import lyncmysql

def decorator(func):
    def wapper(*args):
        sqladmin = 'select user,passwd from admin'
        sqlrst = db.query(sqladmin)
        if len(sqlrst) == 0:
            try:
                admininfo = input('请输入管理员账号密码，以：分割>>>').split(':')
                db.dml("insert into admin(user,passwd) values('{}','{}')".format(admininfo[0],admininfo[1]))
            except IndexError as e:
                print('错误，请以：分割！已退出')
                exit()
        else:

            _user ,_passwd = sqlrst[0]
            passwd = input("请输入管理员密码：")
            cnt = 0
            while passwd != _passwd:
                cnt += 1
                passwd = input("密码错误请重新输入>>>")
                if cnt>1:
                    print("密码错误超过3次，强制退出。。。")
                    exit()
        return func(*args)
    return wapper

@decorator
def zero(info):
    return None

def useradmin():
    sqladmin = 'select user,passwd from admin'
    sqlrst = db.query(sqladmin)
    if len(sqlrst) == 0:
        try:
            admininfo = input('请输入管理员账号密码，以：分割>>>').split(':')
            db.dml("insert into admin(user,passwd) values('{}','{}')".format(admininfo[0],admininfo[1]))
        except IndexError as e:
            print('错误，请以：分割！已退出')
            exit()
    else:
        _user ,_passwd = sqlrst[0]
        passwd = input("请输入管理员密码：")
        cnt = 0
        while passwd != _passwd:
            cnt += 1
            passwd = input("密码错误请重新输入>>>")
            if cnt>1:
                print("密码错误超过3次，强制退出。。。")
                break
                # exit()

@decorator
def add_user(info):
    try:
        if info[0] in userinfo:
            print("用户已存在！请重新输入")
        else:
            db.dml('insert into user values("{}","{}","{}")'.format(info[0],info[1],info[2]))
    except IndexError as e:
        print('错误，请以：分割！ 已返回初始界面')

def list_user(sql):
    data = db.query(sql)
    # print(data)
    for i in data:
        userinfo[i[0]] = list(i)
    return userinfo

def sort_user(sql):
    sortway = ['name', 'age', 'connection']
    for index, item in enumerate(sortway):
        print('{} -> {}'.format(index + 1, item))
    sortnum = input('请选择排序方式，默认name排序，跳过请Enter >>>')
    cnt = 0
    while True:
        if  sortnum.isdigit() or len(sortnum) == 0 :
            break
        else:
            cnt += 1
            if cnt > 2:
                print('输入次数超3次，返回初始界面！')
                return 0
            sortnum = input("请输入正确的排序编号，如需跳过请回车>>>")
    if not sortnum.isalnum():
        print(list_user(sql))
    else:
        sql = 'select name,age,connection from user order by {}  desc'.format(dict(zip((x + 1 for x in range(3)),sortway)).get(int(sortnum)))
        for i in db.query(sql):
            print(i)

@decorator
def update_user(nameinfo):
    if nameinfo[0] in userinfo:
        db.dml('update user set age = "{}",connection = "{}" where name = "{}"'.format(nameinfo[1],nameinfo[2],nameinfo[0]))
    else:
        input('用户不存在！ enter键继续。。。')

@decorator
def delete_user(username):
    if username in userinfo:
        db.dml('delete from user where name = "{}"'.format(username))
    else:
        input('用户不存在！ enter键继续。。。')

@decorator
def find_user(username):
    if username in userinfo:
        print('{} {}'.format(username,userinfo[username]))
        input('enter 键继续。。。')
    else:
        input('用户不存在！ enter键继续。。。')

# def pass_input(msg = ''):
#     if msg != '':
#         sys.stdout.write(msg)
#     chars = []
#     while True:
#         newchar = msvcrt.getch()
#         if newchar in b'\03\r\n':
#             print('')
#             if newchar in b'\03':
#                 chars = []
#             break
#         elif newchar == b'\x08':
#             if chars:
#                 del chars[-1]
#                 sys.stdout.write('\x08 \x08')
#         else:
#             chars.append(newchar)
#             sys.stdout.write('*')
#     return ''.join(x.decode() for x in chars)

if __name__ == '__main__':

    dbconfig = {'host': '10.10.3.128',
                'port': 3306,
                'user': 'repl',
                'passwd': '123',
                'db': 'python',
                'charset': 'utf8'}
    sql = 'select name,age,connection from user order by name  desc '
    db = lyncmysql(dbconfig)
    zero('')
    # pass_input('请输入admin密码>>>')
    # useradmin()
    list1 =['exit','delete', 'update', 'find', 'list','add']
    method = {
        '0': exit,
        '1':delete_user,'2':update_user,
        '3':find_user,'4':list_user,
        '5':add_user
    }

    while True:
        userinfo = {}
        if len(list_user(sql)) == 0:
            print("请输入用户名，年龄，联系方式，以:分开")
            info = list(input('>>>').replace(':', ' ').split(' '))
            db.dml('''insert into user values ('{}' ,{} ,'{}');'''.format(info[0], info[1], info[2]))
        for index ,item in enumerate(list1):
            print('{} -> {}'.format(index,item))
        nums = input('请选择功能>>>')
        if nums == '0':
            break
        elif nums == '4':
            sort_user(sql)
            input('enter 键继续。。。')
        elif nums == '2' or nums == '5':
            nameinfo=list(input('请输入用户名，年龄，联系方式，以:分开>>>').replace(':', ' ').split(' '))
            method.get(nums)(nameinfo)
        elif len(nums) == 0 :
            print("请输入相对应的功能编号")
            continue
        else:
            nameinfo = input('请输入用户名>>>')
            method.get(nums)(nameinfo)


# 装饰器的方式，用的不错，逻辑上没有什么问题


