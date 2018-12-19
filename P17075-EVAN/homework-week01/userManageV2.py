from operator import itemgetter, attrgetter
def userdel():
    name = input('请输入一个用户名:').lower()
    length = len(userInfo)
    for i in range(length):
        if name in userInfo[i]:
            userInfo.remove(userInfo[i])
            break
        else:
            print('查无此人')
            continue

def useradd():
    print('请按此格式输入>>>姓名:年龄:联系方式')
    newUser = input().lower().split(':')
    userInfo.extend([newUser])

def userupdate():
    print('请按此格式输入>>>姓名:年龄:联系方式')
    newUser = input().lower().split(':')
    length = len(userInfo)
    for i in range(length):
        if newUser[0] in userInfo[i]:
            userInfo[i]=newUser
            break
        elif i == length-1:
            print('用户',newUser[0],'不存在')

def userfind():
    name = input('请输入一个用户名:').lower()
    length = len(userInfo)
    for i in range(length):
        if name in userInfo[i]:
            print(userInfo[i])
            break
        elif i == length-1:
            print('查无此人')

def userPrt():
    length = len(userInfo)
    for i in range(length):
        print(userInfo[i])
def funSort():
    sortcmd = input('请输入排序依据：name,age,cont').lower()
    if sortcmd == 'name':
        sortcmd(userInfo,key=itemgetter(0))
    if sortcmd == 'age':
        sortcmd(userInfo, key=itemgetter(1))
    if sortcmd == 'age':
        sortcmd(userInfo, key=itemgetter(2))
    else:
        print('参数错误')

userInfo = [['zhangsan','18','13533333333'],['lishi','22','13733333333'],['wangwu','38','12344444444'],['zhaoliu','44','13788228888']]
pwd1 = input('请初化始管理员密码:')
print('系统启动....')
print('用户信息格式 >>> 姓名:年龄:联系方式')
while True:
    print('命令例表：add,delete,update,find,list,exit,sort')
    cmd = input("请输入一个命令:").lower()
    if cmd in ['add','delete','update','find','list']:
        pwd2 = input('请输入管理员密码：')
        if pwd1 == pwd2:
            if cmd == 'delete':
                userdel()
            if cmd == 'add':
                useradd()
            if cmd == 'update':
                userupdate()
            if cmd == 'find':
                userfind()
            if cmd == 'list':
                userPrt()
#            if cmd == 'exit':
#                print('系统开始退出...')
#                break
        else:
            print('密码错误，系统退出。')
            break
    elif cmd == 'exit':
        print('系统开始退出...')
        break
    elif cmd == 'sort':
        sortcmd = input('请输入排序依据：name,age,cont').lower()
        if sortcmd == 'name':
            pass
        if sortcmd == 'age':
            pass
        if sortcmd == 'cont':
            pass

    else:
        print('命令不存在，请重新输入：')

