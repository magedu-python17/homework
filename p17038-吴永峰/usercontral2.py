# from collections import OrderedDict

import msvcrt,pickle,os

userdict =dict()
# userdict[" name "] = [" age "," tel "]
pawd = []

# 删除用户信息


def deleteuser():
    name = input("请输入您想删除的用户名>>")
    userdict.pop(name,"用户不存在")
    return

# 添加用户信息


def adduser():
    addperson = input("请按这个格式输入用户信息》》 名字：年龄：电话")
    s = addperson.split(":")
    s[1], s[2] = int(s[1]), int(s[2])
    userdict[s[0]] = list(s[1:])
    return


# 查找用户信息


def finduser():
    findername = input("请输入您想查找的用户名字:")

    if findername not in userdict:
        print("user not exist")
    else:
        print("{} : {} : {}".format(findername, userdict[findername][0],userdict[findername][1]))


# 显示所有用户信息


def showusers():
    print("   名字   :", "年龄:", " 联系方式  ")
    for k,v in userdict.items():
        print("{:^10}:{:^5}:{:^}".format(k, v[0], v[1]))



# 更新用户信息
def userupdate():
    new_info = input("请按这个格式输入您想更新的用户信息》》 名字：年龄：电话")
    s = new_info.split(":")
    s[1], s[2] = int(s[1]), int(s[2])
    if s[0] not in userdict.keys():
        print("用户不存在")
    else:
        userdict.update({s[0]:[s[1],s[2]]})


#根据管理员需求进行排序
def usersort():
    print("""
             1.姓名,
             2.年龄,
             3.联系方式""")
    sortbase = int(input("请选择您想排序的选项数字>>>"))
    if sortbase == 2:
        print(sorted(userdict.items(),key=lambda x: x[1][0]))
    if sortbase == 3:
        print(sorted(userdict.items(),key=lambda x: x[1][1]))
    else:
        print(sorted(userdict.items(),key=lambda x: x[0]))


def setpasswd():

    while True:
        first  = input("首次登录请设置密码》》》")
        second = input("请再输入一次》》")
        if first == second:
            pawd.append(first)
            break
        else:
            continue


if os.path.exists("F:/userdict.pkl"):
    with open("F:/userdict.pkl", "rb") as f:
        userdict = pickle.load(f)
        pawd = pickle.load(f)
        f.close()
else:
    print("第一次登录请添加用户》》：")
    adduser()
    setpasswd()


count = 3
while count:
    pwd = input("进行操作前请输入密码》》：")
    if pwd == pawd[0]:
        print("密码输入正确")
        break
    else:
        count -= 1
        print('密码输入错误，您还有{}次机会'.format(count))
        continue


while True:

    print("""
    1:删除
    2：添加
    3：查找
    4：显示用户信息
    5：更新用户信息
    6:用户排序
    7：保存并退出
    """)


    choice = int(input("请输入您的选项："))

    if choice == 7:
         print("即将保存数据退出系统。。。")
         with open("F:/userdict.pkl", "wb") as f:
             pickle.dump(userdict,f)
             pickle.dump(pawd,f,-1)
             f.close()
         break
    if choice == 1:
        deleteuser()
    if choice == 2:
        adduser()
    if choice == 3:
         finduser()
    if choice == 4:
         showusers()
    if choice == 5:
        userupdate()
    if choice == 6:
        usersort()
# 逻辑上没有什么问题，最好每次提交作业的时候加个目录，还有验证用户权限的没有写哈，记得补上