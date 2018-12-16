# 报告老师，可能是我没基础，当前所有的知识储备就是听课听到第14节的知识。
# 课程都是听懂的状态，但可能脑海里还没有知识系统的成型，所以拿到题目毫无概念。
# 在github看了一圈别的同学的作业，36号的Gary同学写的特别清楚，超白痴的我基本能看懂哈。
# 我就先理解了一下他的作业，仿写抄袭了一下嘤嘤嘤~

#定义1个字典，作为用户信息的数据类型。key是用户名，val是其他信息组成的列表。
dict = {}

while True:

    if len(dict) == 0:  #如果字典为空，提示用户先添加数据。

        # 本题精华出现了！！！我已经背出了！！！
        # 用户输入3个值，分别复制给username，age，phone（醍醐灌顶的地方）
        username,age,phone= input('当前无数据\n请输入一组用户名，年龄及联系方式，用":"分开>>').split(':')
        dict[username] = [age, phone]
        #print(dict)

    else:    #字典不为空，提示用户选择 增删改查。
        choice = input('\n回复1：删除用户信息\n'
                       '回复2：更新用户信息\n'
                       '回复3：查找用户信息\n'
                       '回复4：查看所有用户信息\n'
                       '回复5：增加用户信息\n'
                       '回复6：退出系统\n')

        if choice == '1':   # 进行delete
            delete_name = input('请输入你要删除的用户名')
            if delete_name in dict:
                del dict[delete_name]
                #print(dict)
            else:
                print('该用户不存在，无法删除哦')


        elif choice == '2':     #进行update
             update_name,update_age,update_phone = input('请输入要更新的用户名，年龄及联系方式，用":"分开>>').split(':')
             if update_name in dict:
                 dict[update_name] = [update_age, update_phone]
                 #print(dict)
             else:
                print('no user')


        elif choice == '3':     # 进行find
            find_name = input('请输入你要查找的用户名')
            if find_name in dict:
                print('用户名{}，年龄{}，电话{}'.format(find_name, dict[find_name][0], dict[find_name][1]))
            else:
                print('找不到该用户')


        elif choice == '4':     # 进行list，依次打印用items。
            print('用户名   年龄    电话')
            for k, val in dict.items():
                 print('  {}     {}      {}'.format(k, val[0], val[1]))


        elif choice == '5':     #进行add，设计了可以1次添加多组。
            num = input('你要添加几组数据呢：')
            for i in range(int(num)):
                add_username, add_age, add_phone = input('请输入用户名，年龄及联系方式，用":"分开>>').split(':')
                dict[add_username] = [add_age, add_phone]
            print(dict)


        elif choice == '6':     #退出循环。
            print('数据已保存')
            break
