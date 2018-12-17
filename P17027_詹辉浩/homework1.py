import time
import sys
import random

# 用来生成初始化数据的类
class Utils:
    # 初次生成信息
    # {'Username': 'fjfsk', 'age': 59, 'phone': '17580941542'}
    @classmethod
    def _generatedict(cls, count=10):
        while count:
            count -= 1
            yield {'Username': next(cls._genusername()), 'age': next(cls._genage()), 'phone': next(cls._genphone())}

    # 生成随机用户名
    @classmethod
    def _genusername(cls):
        while True:
            yield ''.join([chr(random.randint(97,122)) for _ in range(5)])

    # 生成随机年龄
    @classmethod
    def _genage(cls):
        while True:
            yield random.randint(1,100)

    # 生成随机手机号码
    @classmethod
    def _genphone(cls):
        while True:
            yield ''.join([str(random.randint(0,9)) for _ in range(11)])

class UserManagerSystem:

    # 用来生成初始用户数据，默认十条，可以在Utils._generatedict()中修改，例如Utils._generatedict(20)
    def __init__(self):
        self.record = [ record for record in Utils._generatedict() ]

    # 用来输出表头信息的方法
    def print_user_title(self):
        print()
        print("|     UserId     ||     UserName     ||     Age     ||        Phone        |")
        print("-"*80)

    # 增加用户的功能
    # TODO 没有判断用户输入的信息是否合规功能
    def add(self):
        userinfo = input("[ add ] pls input information you want to add like 'Username:Age:Phone' >>>")
        username, age, phone = userinfo.split(":")

        record = {'Username':username, 'age':age, 'phone':phone}
        self.record.append(record)
        self.list()

    # 列出所有用户的功能
    def list(self):
        self.print_user_title()
        for i, items in enumerate(self.record):
            print("|{:^16}||{:^18}||{:^13}||{:^21}|".format(i, items['Username'], items['age'], items['phone']))
        print()

    # 更新用户信息的功能
    # TODO 没有判断用户输入的信息是否合规功能
    def update(self):
        userinfo = input("[ update ] pls input info you want to update like 'username:age:phone' >>>")
        username, age, phone = userinfo.split(":")

        match, index, userinfo = self.check_user_status(username)

        if match:
            userinfo['Username'] = username
            userinfo['age'] = age
            userinfo['phone'] = phone
            print('all update are done...')
            self.list()

    # 删除用户信息的功能
    def delete(self):
        username = input("[ delete ] pls input username you want to delete >>>")
        match, index, userinfo = self.check_user_status(username)

        if match:
            self.record.pop(index)
            self.list()

    # 查找用户的功能
    def find(self):
        while True:
            username = input("[ find ] pls input username you want to search>>>")
            match, index, userinfo = self.check_user_status(username)

            if match:
                self.print_user_title()
                print("|{:^16}||{:^18}||{:^13}||{:^21}|\n".format(index, userinfo['Username'], userinfo['age'], userinfo['phone']))

            # 是否继续查找功能
            ops = input("Do you want to continue to search other user? Y/n").strip()
            if ops not in 'Yy':
                break

    # 检查用户是否存在,并返回<用户状态>，<用户信息在列表的下标>，<用户的信息>
    # 这里主要是解决find、delete、update功能都需要检查用户是否存在
    # 增强代码的复用性
    def check_user_status(self, username):
        match = False
        index = 0
        userinfo = ""

        for i, record in enumerate(self.record):
            if username == record['Username']:
                match = True
                index = i
                userinfo = self.record[index]
                break

        if match:
            return match, index, userinfo
        else:
            print('\nUser < {} > no found in system\n'.format(username))
            return None,None,None

    # 退出功能
    def exit(self):
        print('saving your data...')
        time.sleep(1)
        print('exiting...')
        sys.exit(0)

    # 系统命令没有找到时，默认打印的字符串
    def default_print(self):
        print('\n[ ERROR ] ilegal command, only allow in [ add | delete | update | find | list | exit ]\n')

    # 欢迎交互功能
    def welcome(self):
        print("""
        ==========================================================
        |>>>    Welcome Use Magedu <User Manager System>!
        ==========================================================
        """)

        while True:

            cmd = input("[ system ] pls input your options>>>")
            getattr(self, cmd, self.default_print)()


if __name__ == '__main__':
    p1 = UserManagerSystem()
    p1.welcome()

# 少个提示操作的菜单，别的没有啥问题，再来个对用户操作的时候，加个验证密码，比如首次运行时候，add 和 update 和delete的等操作的时候，需要验证管理员密码