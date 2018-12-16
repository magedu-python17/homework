import json
from dbconn import lyncdb
# userinfo ={'2': ['f', '3'],'3':['e','4']}  # 用户名 年龄  联系方式

def add_user(info):
    userinfo[info[0]] = info[1:]
    print(userinfo)  # 保存用户信息
def delete_user(username):
    if username in userinfo:
        db.dml('delete from user where name = "{}"'.format(username))
    else:
        input('用户不存在！ enter键继续。。。')

def update_user(nameinfo):
    if nameinfo[0] in userinfo:
        db.dml('update user set age = "{}",connection = "{}" where name = "{}"'.format(nameinfo[1],nameinfo[2],nameinfo[0]))
    else:
        input('用户不存在！ enter键继续。。。')

def find_user(username):
    if username in userinfo:
        print('{} {}'.format(username,userinfo[username]))
        input('enter 键继续。。。')
    else:
        input('用户不存在！ enter键继续。。。')

def list_user():
    print('用户行为信息描述:')
    sql = 'select name,age,connection from user'
    data = db.query(sql)
    for i in data:
        userinfo[i[0]] = list(i[1:])
    return userinfo

if __name__ == '__main__':
    dbconfig = {'host': '10.10.3.128',
                'port': 3306,
                'user': 'repl',
                'passwd': '123',
                'db': 'python',
                'charset': 'utf8'}
    db=lyncmysql(dbconfig)

    list1 =['delete', 'update', 'find', 'list','exit']
    method = {
        '1':delete_user,'2':update_user,
        '3':find_user,'4':list_user,
        '5':exit
    }

    while True:
        userinfo = {}
        if len(list_user()) == 0:
            print("请输入用户名，年龄，联系方式，以:分开")
            info = list(input('>>>').replace(':', ' ').split(' '))
            db.dml('''insert into user values ('{}' ,{} ,'{}');'''.format(info[0], info[1], info[2]))

        for index ,item in enumerate(list1):
            print('{} -> {}'.format(index+1,item))
        nums = input('请选择功能>>>')
        if nums == '5':
            break
        elif nums == '4':
            print(json.dumps(list_user(), sort_keys=True, indent=4))
            input('enter 键继续。。。')
        elif nums == '2':
            nameinfo=list(input('请输入用户名，年龄，联系方式，以:分开>>>').replace(':', ' ').split(' '))
            method.get(nums)(nameinfo)
        else:
            nameinfo = input('请输入用户名>>>')
            method.get(nums)(nameinfo)



