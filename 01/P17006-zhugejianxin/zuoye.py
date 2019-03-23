#! /usr/bin/env python
from pathlib import Path
import json
from functools import partial


class UserManager:

    def __init__(self):
        self.__uc = {}
        self.__default_dir = 'user_conf.json'
        self.__save_dir = self.__default_dir

    def _modify(self, con):
        info = input("    Tips: colon-separated value for one user,comma-separated user for multi-user (用户名:年龄:联系方式)\n>>>")
        lst = info.strip(',: ').split(',')
        for us in lst:
            user = us.strip(',: ').split(':')
            if len(user) != 3:
                continue
            if (con == 'add') != (self.__uc.get(user[0], False)):
                self.__uc[user[0]] = user[1:3]
            elif con == 'add':
                print('User "{}" exists already, fail to "add", please use "update" when user exists'.format(user[0]))
            else:
                print('User "{}" not exists, fail to "update", please use "add" when user not exists'.format(user[0]))

    def add_update(self, mode='add'):
        return partial(self._modify, con=mode)

    def find(self):
        fu = input("User to find>>>")
        if self.__uc.get(fu, None):
            print("{:20}{:5}{:15}".format('username', 'age', 'tel'))
            print("{:20}{:5}{:15}".format(fu, self.__uc[fu][0], self.__uc[fu][1]))
        else:
            print('User "{}" not exist'.format(fu))

    def delete(self):
        ru = input('User to delete>>>')
        if self.__uc.get(ru, None):
            del self.__uc[ru]
        else:
            print('User "{}" not exists, fail to delete'.format(ru))

    def list(self):
        sc = input('    Tips: colon separate key with reverse, "username" is default for key and False is default for reverse if no entry(age:y)\n>>>')
        sl = sc.rstrip(', :').split(':')
        rev = False if len(sl) == 1 or sl[1] == '' else True
        k = 'username' if sl[0] == '' else sl[0]
        if k == 'age':
            user_ge = (i for i in sorted(self.__uc, key=lambda x: self.__uc[x][0], reverse=rev))
        elif k == 'tel':
            user_ge = (i for i in sorted(self.__uc, key=lambda x: self.__uc[x][1], reverse=rev))
        else:
            user_ge = (i for i in sorted(self.__uc, reverse=rev))
        print("{:20}{:5}{:15}".format('username', 'age', 'tel'))
        for lu in user_ge:
            print("{:20}{:5}{:15}".format(lu, self.__uc[lu][0], self.__uc[lu][1]))

    def exit(self):
        sp = input("path to save data:(no entry for default)>>>")
        self.__save_dir = sp if sp else self.__default_dir
        with open(self.__save_dir, 'w') as f1:
            json.dump(self.__uc, f1)
        print('data saved to "{}" completely, bye-bye!'.format(Path(self.__save_dir).resolve()))

    def load(self):
        lp = input('path to load data:(no entry for default)>>>')
        p = Path(lp)
        op = lp if p.exists() and p.suffix == '.json' else self.__save_dir
        with open(op) as rf:
            get = json.load(rf)
        self.__uc.update(get)
        print('load date from "{}"succeed'.format(Path(op).resolve()))

    def check_empty(self):
        if not self.__uc:
            print('    Tips: No data,please add or load')


command = ['add', 'update', 'find', 'delete', 'list', 'exit', 'load', 'help']


def tip():
    print("    Tips: valid command: {}".format(' '.join(command)))


def illegal_cmd():
    print("illegal command, input 'help' to get help")
    tip()


um = UserManager()
func = [um.add_update(mode='add'), um.add_update(mode='update'), um.find, um.delete, um.list, um.exit, um.load, tip]
register = dict(zip(command, func))
while True:
    um.check_empty()
    cmd = input("Command >>> ")
    register.get(cmd, illegal_cmd)()
    if cmd == 'exit':
        break

# 这写的没有什么问题