# 自己写的时候,列表存放方式是一层,在列表取值部分卡住了。
# 参考了下P17007-zhide.zhang同学写的,并参考仿写了一下,明白了如何使用列表内嵌套列表

user_info = []
while True:
    if len(user_info) == 0:
        tmp = input("当前没有用户,请添加用户信息\n用户信息格式'username:age:tel': ")
        if tmp.count(':') == 2:
            user_info.append(tmp.split(':'))
            print("添加的用户信息已保存")
        elif tmp == 'exit':
            print("退出")
            break
        else:
            print("输入格式有误,请重新输入")
    else:
        command = input("请输入你的操作 [add|delete|update|find|list|exit] :")
        if command == 'add':
            user_info.append(input("请输入要添加的用户信息,用户信息格式 'username:age:tel':").split(':'))
            print("添加的用户信息已保存")
        elif command == 'delete':
            deluser = input("请输入要删除的用户名: ")
            for i in range(len(user_info)):
                if deluser == user_info[i][0]:
                    user_info.remove(user_info[i])
                    print("删除用户",deluser,"成功")
                    break
            else:
                print("用户不存在")
        elif command == 'update':
            up_user = input("请输入要更新的用户信息,用户信息格式'username:age:tel': ").split(':')
            for i in range(len(user_info)):
                if up_user[0] == user_info[i][0]:
                    user_info[i] = up_user
                    print("用户",up_user[0],"信息更新成功")
                    break
            else:
                print("用户不存在")
        elif command == 'find':
            fuser = input("请输入要查找的用户名: ")
            for i in range(len(user_info)):
                if fuser == user_info[i][0]:
                    print("{:12}    {:12}    {:12}".format('name', 'age', 'tel'))
                    print("{:12}    {:12}    {:12}".format(user_info[i][0],user_info[i][1],user_info[i][2]))
                    break
            else:
                print("用户不存在")
        elif command == 'list':
            print("{:12}    {:12}    {:12}".format('name','age','tel'))
            for i in range(len(user_info)):
                print("{:12}    {:12}    {:12}".format(user_info[i][0],user_info[i][1],user_info[i][2]))
        elif command == 'exit':
            print("用户信息已更新,退出")
            break
        else:
            print("输入错误请重新输入")