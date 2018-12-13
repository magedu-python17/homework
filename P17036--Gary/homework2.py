#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/12/12'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

# 导入相关的模块
import time
import random
import datetime

# 定义保存用户信息的数据类型，字典中嵌套列表
dic_name = {}

# 获取当前系统的时间
st = datetime.datetime.now()

# 用户界面
def menu():
    print('欢迎进入用户管理系统'.center(60,'*'))
    print('当前时间:{}-{}-{} {}:{}:{}   星期    {}'.format(st.year,st.month,st.day,st.hour,st.minute,st.second,st.weekday()).center(60,' '))
    print(''.center(70,'*'))
    print('delete:删除用户  '.center(60,' '))
    print('update:更新用户的数据'.center(60,' '))
    print('find:查找用户     '.center(60,' '))
    print('list:显示用户信息  '.center(60,' '))
    print('add:添加用户信息  '.center(60,' '))
    print('exit:退出      '.center(60,' '))
    print(''.center(70,'*'))


# 主函数
def main():
    while True:
        menu()
        # 判断字典是否为空,为空首先输入用户的信息，否则进入后面的操作
        if len(dic_name) < 1:
            print('系统暂时没有用户信息，请添加信息！')
            username,age,phone_number = input('请输入用户名，年龄及联系方式，用空格分开>>').split(' ')
            # 把用户信息保存在一个临时列表中，把临时列表信息添加到字典中
            ls_temp = [age,phone_number]
            dic_name[username] = ls_temp
            print('添加的信息如下...')
            # print('用户    年龄    联系方式:')
            print('用户名:{}  年龄:{}  联系方式:{}'.format(username,ls_temp[0],ls_temp[1]))
        else:
            choise_number = input('请输入你想要操作的选项>>')

            # 删除用户信息
            if choise_number.lower() == 'delete':

                name = input('请输入用户名>>')
                # 判断输入的用户是否在字典中
                # 已经判断了用户是否在字典中，故不用考虑删除字典数据抛异常的情况
                if name in dic_name:
                    # try:
                        print('正在删除{}用户的信息...'.format(name))
                        time.sleep(random.randint(1,3))
                    #     dic_name.pop(name)
                    #     print('删除成功...')
                    # except:
                    #     print('抛异常...')
                    #     print('字典为空。。。。')
                else:
                    print('正在查找{}用户的信息...'.format(name))
                    time.sleep(random.randint(4,8))
                    print('哎呦，我都跑到月球上去找了，还是没有找您要删除的用户信息...')

            elif choise_number.lower() == 'update':
                # print(choise_number)
                username,age,phone_number = input('请输入用户名，年龄及联系方式').split(' ')
                for k in dic_name.keys():
                    # 由于用户的年龄和联系方式是保存在列表中，故通过键直接赋值
                    if k == username:
                        dic_name[k][0] = age
                        dic_name[k][1] = phone_number
                        print('用户的信息正在更新....')
                        # 假装在更新用户信息，更新的时间随机。。。。
                        time.sleep(random.randint(2,6))
                        print('用户的信息已更新完成...')
                    else:
                        print('你输入的用户不存在（更新）!')
            elif choise_number.lower() == 'find':
                name = input('请输入用户名>>')

                # 这个地方很容易出现BUG，判断是否存在，判断不存在的话会多打印几次
                # for k in dic_name.keys():
                #     Flag = False
                # # if  name in dic_name:
                #     if k == name:
                #         print('找到你要查找的用户信息...')
                #         print('请稍后，正在查找你需要的信息...')
                #         time.sleep(random.randint(1,4))
                #         print('查到的信息如下...')
                #         # print('用户    年龄    联系方式:')
                #         print('用户名:{}    年龄:{}    联系方式:{}'.format(name,dic_name[k][0],dic_name[k][1]))
                #         Flag = True
                #
                #     else:
                #          # if flag =
                #          print('你查找的用户不存在（find）!')


                #进一步进行优化，先遍历字典中是否存在这个用户，存在设置一个遍历为真，否则为假
                #根据变量来判断是否找到
                Flag = False
                for k in dic_name.keys():
                    if k == name:
                        Flag = True
                    else:
                        Flag = False

                print('请稍后，正在查找你需要的信息...')

                # 根据标志判断字典中是否有用户的信息

                if Flag:
                    print('系统里面有您要查找的用户信息...')
                    time.sleep(random.randint(1,4))
                    print('查到的信息如下...')
                    print('用户名:{}    年龄:{}    联系方式:{}'.format(name,dic_name[k][0],dic_name[k][1]))
                else:
                    # print('你查找的用户不存在（find）!')
                    time.sleep(random.randint(6,9))
                    print('哎呦，我都跑到火星上找了，还是没有找到您要找的用户信息...')


            elif choise_number.lower() == 'list':
                # 打印用户信息
                print('用户        年龄        联系方式:')
                for k,v in dic_name.items():
                    print('{}      {}     {}'.format(k,v[0],v[1]))

            elif choise_number.lower() == 'exit':
                print('您已经保存了修改的数据，谢谢您本次的使用,期待您再一次的使用！')
                exit()

            elif choise_number.lower() == 'add':
                print(choise_number)
                username,age,phone_number = input('请输入用户名，年龄及联系方式，用空格分开>>').split(' ')
                print('开始向系统中添加用户信息....')
                time.sleep(random.randint(2,4))
                ls_temp = [age,phone_number]
                dic_name[username] = ls_temp
                # dic_name[username][0] = age
                # dic_name[username][1] = phone_number
                print('添加的信息如下....')
                print('用户名:{}    年龄:{}    联系方式:{}'.format(username,ls_temp[0],ls_temp[1]))
                print('添加的信息已经完成！')


if __name__=="__main__":
    main()
