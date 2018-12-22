import json
import getpass

class run():

    def __init__(self):
        self.filename = 'store_file.json'
        self.passwd = 'passwd_file.json'
        self.action_dict = {
            'delete': self.new_delete,
            'update': self.new_update,
            'find': self.new_find,
            'show': self.new_show,
            'exit': self.new_exit
        }

    def new_delete(self):
        user = input('请输入需要删除的用户名：').strip('\r')
        for k,v in self.new_dict.items():
            if user == v["username"]:
                del self.new_dict[k]
                break
        else:
            print('您想删除的用户不存在')

    def new_update(self):
        num_max = 0
        for k, v in self.new_dict.items():
            if int(k) > num_max:
                num_max = int(k)

        # if num_max == 0:
        #     print('无用户，请提交数据')
        num_max += 1
        print('输入格式： 用户名:年龄:联系方式')
        user,age,tel = input('>>> ').split(':')
        self.new_dict[str(num_max)] = {
          "username": user,
          "age":age,
          "tel":tel
              }


    def new_find(self):
        user = input('请输入需要查找的用户名：')
        for k,v in self.new_dict.items():
            if user == v["username"]:
                print('用户名:{} 年龄:{} 电话:{}'.format(v["username"],v["age"],v['tel']))
                break
        else:
            print('用户没找到')

    def new_show(self):
        if self.new_dict:
            print('{:>20} |{:>20} |{:>20}'.format('username', 'age', 'tel'))
            field = input('请输入想要排序的字段(默认username):')
            if len(field) == 0 or field == 'username':
                for k,v in sorted(self.new_dict.items(),key=lambda e:e[1]['username']):
                    print('{:>20} |{:>20} |{:>20}'.format(v["username"],v["age"],v['tel']))
            else:
                if field == 'age':
                    for k, v in sorted(self.new_dict.items(), key=lambda e: int(e[1]['age'])):
                        print('{:>20} |{:>20} |{:>20}'.format(v["username"], v["age"], v['tel']))
                if field == 'tel':
                    for k, v in sorted(self.new_dict.items(), key=lambda e: int(e[1]['tel'])):
                        print('{:>20} |{:>20} |{:>20}'.format(v["username"], v["age"], v['tel']))

        else:
            print('目前啥都没有')

    def new_exit(self):
        answer = input('请问您想保存现有信息并退出吗？？[y/n]')
        if answer == 'y' or answer == 'Y':
            with open(self.filename, 'w') as fb2:
                fb2.write(json.dumps(self.new_dict, indent=4, sort_keys=True, ensure_ascii=False))
            exit(0)

    def main(self):
        print('程序启动啦！！！')
        with open(self.passwd, 'r') as fb:
            self.passwd_dict = json.loads(fb.read())
        a = self.passwd_dict.get('password',None)
        if a is None:
            passwd = getpass.getpass('由于是第一次登陆，请输入管理员密码:')
            with open(self.passwd, 'r') as fb2:
                self.passwd_dict = json.loads(fb2.read())
                self.passwd_dict['password'] = passwd
            with open(self.passwd, 'w') as fb3:
                fb3.write(json.dumps(self.passwd_dict, indent=4, sort_keys=True, ensure_ascii=False))
            print('管理员密码设置成功！！！')
        with open(self.filename, 'r') as fb1:
            self.new_dict = json.loads(fb1.read())
            while True:
                action = input(">>> ")
                if not action:
                    continue
                if action in self.action_dict:
                    passwd = getpass.getpass('请输入管理员密码:')
                    if self.passwd_dict['password'] == passwd:
                        func = self.action_dict.get(action)
                        func()
                    else:
                        print('密码输入错误！！！')
                else:
                    print('命令格式: [delete|update|find|show|exit]')


if __name__ == "__main__":
    f = run()
    f.main()