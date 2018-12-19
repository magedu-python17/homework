import json


class run():

    def __init__(self):
        self.filename = 'store_file.json'
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
            for k,v in self.new_dict.items():
                print('{:>20} |{:>20} |{:>20}'.format(v["username"],v["age"],v['tel']))
        else:
            print('目前啥都没有')

    def new_exit(self):
        answer = input('请问您想保存现有信息并退出吗？？[y/n]')
        if answer == 'y' or answer == 'Y':
            with open(self.filename, 'w') as fb2:
                fb2.write(json.dumps(self.new_dict, indent=4, sort_keys=True, ensure_ascii=False))
            exit(0)

    def main(self):
        with open(self.filename, 'r') as fb:
            self.new_dict = json.loads(fb.read())
            while True:
                action = input(">>> ")
                if not action:
                    continue
                if action in self.action_dict:
                    func = self.action_dict.get(action)
                    func()
                else:
                    print('命令格式: [delete|update|find|show|exit]')
            # if action == 'delete':
            #     new_delete()
            # elif action == 'update':
            #     new_update()
            # elif action == 'find':
            #     new_find()
            # elif action == 'show':
            #     new_show()
            # elif action == 'exit':
            #     new_exit()


if __name__ == "__main__":
    f = run()
    f.main()

# 逻辑上没有什么太大的问题，想想用with open 来操作文件的读写 试试