#! /usr/bin/env python
# 实现一个用户管理系统，可以与管理员用户进行交互，根据用户输入的指令(增删改查)，可以进行相应的操作：
# 1.输入delete，则让用户输入”用户名”格式字符串，根据用户名查找内存里面的数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在;
# 2.输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找内存中数据，若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在;
# 3.输入find，则让用户输入”用户名”格式字符串，根据用户名查找内存中数据包含输入字符串的用户信息，并打印;
# 4.输入list，则打印所有用户信息;打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;排序：可以让用户指定排序字段，默认name 排序
# 5.输入exit，则提示用户并且保存已经修改的用户信息，退出程序;
# 注意：首次运行时候或者用户为0的时候，需提示用户先添加数据。
# 6.增加管理员验证功能(即首次运行系统时候，提示管理员设置密码，用户进行 add list delete update find的时候需要验证管理员密码)
from pathlib import Path
import json
import re
import datetime
import getpass
up = """[a-zA-Z0-9_]{1,12}"""
ur = re.compile(up)
tp = """\d{11}"""
tr = re.compile(tp)
time_zone = datetime.timezone(datetime.timedelta(0, 28800))     # 设置时区


# 输入数据预处理 input process
def inp(cmd_s, promote):
    info = input('<{}> ({}) >>> '.format(cmd_s, promote))
    return info.strip(', :')


# 数据检测函数data check
def dck1(names: str):
    names_list = names.split(',')
    buffer = []
    for name_str in names_list:
        name = name_str.strip(' :')
        if ur.fullmatch(name) is None:
            print('  warning: 用户名 "{}" 不规范(1~12位，字母，数字下划线组成)'.format(name))
        else:
            buffer.append(name)
    return buffer


def dck2(fn):             # 数据检测装饰器版本，用于导入数据检查
    def _wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        if isinstance(ret, dict):
            new_ret = {}
            for name, info in ret.items():
                if ur.fullmatch(name) is None:
                    print('  warning: 用户名 "{}" 不规范(1~12位，字母，数字下划线组成)'.format(name))
                elif int(info[0]) < 0 or int(info[0]) > 200:
                    print('  warning: 用户 {} 的年龄: "{}" 不合法(范围[0,200])'.format(name, info[0]))
                elif tr.fullmatch(info[1]) is None:
                    print('  warning: 用户 {} 的手机号: "{}" 格式错误(11位手机号)'.format(name, info[1]))
                else:
                    new_ret[name] = info
            return new_ret
    return _wrapper


def dck3(users_str: str):       # 用于add,update等命令输入用户详细信息的检查
    dic = {}
    users_list = users_str.split(',')
    for user_str in users_list:
        user = user_str.strip(': ').split(':')
        if len(user) != 3:
            print('  warning: 用户信息: "{}" 不规范(姓名:年龄:手机号)'.format(user_str))
        elif ur.fullmatch(user[0]) is None:
            print('  warning: 用户名 "{}" 不规范(1~12位，字母，数字下划线组成)'.format(user[0]))
        elif int(user[1]) < 0 or int(user[1]) > 200:
            print('  warning: 用户 {} 的年龄: "{}" 不合法(范围[0,200])'.format(user[0], user[1]))
        elif tr.fullmatch(user[2]) is None:
            print('  warning: 用户 {} 的手机号: "{}" 格式错误(11位手机号)'.format(user[0], user[2]))
        else:
            dic[user[0]] = user[1:]
    return dic


@dck2
def jfr(fp):                    # json file read，使用json读取文件，并检测数据
    with open(fp) as f:         # TODO 若文件json无法识别的情况未考虑，如文件内容为空
        dic = json.load(f)
    return dic


def out_format1(buffer_yes, buffer_no, tip_yes, tip_no):        # 输出格式化
    print("      {:20}{:5}{:15}{}".format('username', 'age', 'tel', '' if tip_yes is None and tip_no is None else '结果'))
    for name, info in buffer_yes:
        print("      {:20}{:5}{:15}{}".format(name, info[0], info[1], tip_yes if tip_yes is not None else ''))
    for name in buffer_no:
        print("      {:20}{:5}{:15}{}".format('**' + name + '**', '', '', tip_no if tip_no is not None else ''))


def combine(dic1: dict, dic2: dict):
    """
    使用一个字典dic2来更新dic1的数据，有重复的key时提示用户确认，原址修改dic1
    """
    help_info = """正在合并，如果有重复项，请输入以下字符确认是否更新：
    y:   更新当前条目                        n：表示不更新当前条目
    yes: 表示更新当前及之后的所有同名条目       no：表示不更新当前及之后的所有同名条目
    其他: 表示取消当前更新操作"""
    set1 = set(dic1)
    count1 = len(dic1)
    set_in = set()
    set_key = set1.intersection(dic2)       # 两个字典关键字相同的集合(交集)，集合存放的是key(set2)
    for key in set_key:                     # 获取字典不同的key-value对，将key添加到集合set中
        if dic1[key] != dic2[key]:
            set_in.add(key)
    count_in = len(set_in)                  # 统计交集的数量
    n = count_in                            # n用于控制循环
    set_exp = set()                         # 排除项集合，存放不需要更新的key的集合。(set3)
    flag = True
    if count_in:
        print(help_info)
    while n:
        name = set_in.pop()
        n -= 1
        ensure = input('  tip: 重复：是否使用 {0}:{1} 替换 {0}:{2}，后面还有 {3} 个重复项，请确认：>>> '.format(name, ':'.join(dic2[name]), ':'.join(dic1[name]), n))
        if ensure == 'y':
            continue
        elif ensure == 'n':
            set_exp.add(name)
        elif ensure == 'yes':
            break
        elif ensure == 'no':
            set_exp.add(name)
            set_exp.update(set_in)
            break
        else:
            flag = False
            break
    if flag:                            # 先确认后开始更新，如果确认过程中取消操作，原字典不会改变
        for name, info in dic2.items():
            if name not in set_exp:
                dic1[name] = info
        uc = count_in-len(set_exp)        # update count更新计数
        ac = len(dic1)-count1             # add count添加计数
        print('  tip: 数据已合并,成功更新{}条数据，成功添加{}条数据'.format(uc, ac))
        return dic1
    else:
        print('  tip: 已取消本次合并操作')
        return dic1                     # 返回原字典


class UserManager:
    """
    命令模式：
        load:   加载用户数据，由用户指定导入文件位置（注意文件需以.json结尾,请谨慎操作）
        add:    添加用户信息，添加单个用户信息使用冒号隔开(用户名:年龄:联系方式)，一次添加多个用户使用逗号隔开
        update: 更新用户信息，更新单个用户信息使用冒号隔开(用户名:年龄:联系方式),一次更新多个用户使用逗号隔开
        delete: 删除用户信息，输入用户名，回显详细信息，提示是否确认删除；一次删除多个用户可以使用逗号隔开
        find:   查找用户信息，输入用户名，显示匹配的用户信息；一次查找多个用户可以使用逗号隔开
        list:   打印用户信息,输入排序关键字即是否升序，以冒号隔开，关键字不输入或不存在即默认用户名排序；y表示升序，缺省或其他任意字符表示默认降序（如输入:y）
        help:   查看命令帮组信息
    数据：
        其他字符：判断字符是否合法，若合法，则送给命令执行
        q!:     退出当前命令模式，提示用户输入命令后进入该命令模式（如输入add命令，再输入数据后不会退出add命令，可以不用再输入add而继续添加数据）
    退出管理系统：
        exit:   退出管理系统，并保存到指定位置
    """

    def __init__(self):
        self.__uc = {}                  # user_config 用户信息 {'用户名': [年龄， 练习方式]}
        self.__pw = ''                  # 管理员密码
        self.__login_status = False     # 判断用户是否是在登录时要求输入密码，还是在执行命令时要求输入密码
        self.__pwd_status = True        # 上一次是否密码是否输入正确，如果不正确(即false)，等待三分钟才可以
        self.__pwd_time = datetime.datetime.fromtimestamp(0, tz=time_zone)      # 上一次密码错误时间
        self.__default_dir = 'user_conf.json'
        self.__save_dir = self.__default_dir
        self.__config_dir = 'admin.conf'
        # 用户数据采用字典的形式保存：格式为{'username',['age', 'tel']}
        # 系统配置信息采用列表的形式保存：格式为['密码', '是否已登录', '上一次是否正确输入密码', '输入三次错误密码的时间']

    def verify(self):
        if self.__pw == '':
            print(' tip: 首次登录请设置管理员密码（至少6位）')
            while True:
                pwd = getpass.getpass('Set password: ')
                if len(pwd) >= 6:
                    self.__pw = pwd
                    print('  tip: 成功设置管理员密码')
                    break
                else:
                    print('  tip: 确保密码至少6位！')
        count = 3               # 表示有三次尝试机会
        while True:
            pwd = getpass.getpass('Enter password')
            flag = False
            if self.__pwd_status and count > 0:         # 上一次登录正常登录，且还有尝试密码机会
                count -= 1
                if pwd == self.__pw:
                    flag = True
                else:
                    print('  warning: 密码错误，还有{}次机会，'.format(count))
            if not flag and count <= 0:                            # 密码尝试三次依然错误
                self.__pwd_status = False
                self.__pwd_time = datetime.datetime.now(tz=time_zone)
                count = 3                               # 重置计数器count
                if self.__login_status is True:         # 如果此时已经登录系统，表示执行命令时输错三次，返回False状态码
                    print('  warning: 密码验证不通过，无法执行')
                    return False
            if not flag and self.__pwd_status is False:                                       # 上一次登录失败
                now = datetime.datetime.now(tz=time_zone)
                delta = (now-self.__pwd_time).total_seconds()
                if delta <= 180:
                    print('  tip: 由于上次登录输错 3 次密码，还需等待{}s后才可验证'.format(int(180 - delta)))
                else:
                    self.__pwd_status = True
            if flag:                                    # 密码正确
                if self.__login_status is False:
                    self.__login_status = True
                print('  tip: 密码验证通过{}'.format('，正在登录系统' if self.__login_status is False else ''))
                return True

    def startup(self):
        p = Path(self.__config_dir)
        if p.exists() and p.stat().st_size != 0:         # 读取系统配置文件信息
            with open(self.__config_dir) as f:
                get_config = json.load(f)
            self.__pw = get_config[0]
            self.__login_status = get_config[1]
            self.__pwd_status = get_config[2]
            self.__pwd_time = datetime.datetime.strptime(get_config[3], '%Y%m%d %H:%M:%S%z')
        print('                    欢迎使用用户信息管理系统')
        self.verify()                                    # 密码认证
        if self.__login_status:                          # 认证成功时，self.__login_status状态码变为True
            p = Path(self.__save_dir)
            if p.exists() and p.stat().st_size == 0:     # 读取用户数据
                with open(self.__save_dir, 'w') as f:
                    json.dump({}, f)
                self.__uc = {}
            elif p.exists() and p.stat().st_size != 0:
                self.__uc = jfr(self.__save_dir)
            else:
                p.touch()
                with p.open('w') as f:
                    json.dump({}, f)
                self.__uc = {}
            if self.__uc:               # 用户的配置信息为空时，提醒用户
                print('  tip: 系统初始化完毕，enjoy it!')
            else:
                print('  tip: 系统初始化完毕，当前无数据，请添加或导入数据，输入help命令可查看帮组信息：')

    def add(self, dic):
        add_yes = []         # 存放需要添加的用户，主要用于回显结果
        add_no = []          # 存放系统已经存在，不能add的用户，用于回显结果
        for name, info in dic.items():
            if self.__uc.get(name, None):
                add_no.append(name)
            else:
                self.__uc[name] = info
                add_yes.append((name, info))
        out_format1(add_yes, add_no, '已添加', '用户已存在，添加失败')

    def update(self, dic):
        update_yes = []
        update_no = []
        for name, info in dic.items():
            if self.__uc.get(name, None):
                self.__uc[name] = info
                update_yes.append((name, info))
            else:
                update_no.append(name)
        out_format1(update_yes, update_no, '已更新', '用户不存在，更新失败')

    def find(self, names):
        find_yes = []
        find_no = []
        for name in names:
            if self.__uc.get(name, None):
                find_yes.append((name, self.__uc[name]))
            else:
                find_no.append(name)
        out_format1(find_yes, find_no, '已找到', '用户不存在，无法查询')

    def delete(self, names):
        delete_yes = []
        delete_no = []
        for name in names:
            if self.__uc.get(name, None):
                ensure = input('  tip:确认删除用户: {}:{}？(yes: 删除 | 其他:保留，不删除) >>> '.format(name, ':'.join(self.__uc[name])))
                if ensure == 'yes':
                    delete_yes.append((name, self.__uc[name]))
                    del self.__uc[name]
                    continue
            delete_no.append(name)
        out_format1(delete_yes, delete_no, '已删除', '删除失败，用户不存在或取消删除操作')

    def list(self, sort_str: str):           # 用户可以输入age:y , :y ,  y，或空。过滤后sort_str收到age:y  y  y  ''
        sort_info = sort_str.split(':')
        sort_func = {
            'age': lambda x: int(self.__uc[x][0]),
            'tel': lambda x: int(self.__uc[x][1])
        }
        sort_key = sort_info[0] if sort_info[0] in sort_func else 'username'
        sort_rev = True if len(sort_info) == 2 and sort_info[1] == 'y' or sort_info[0] == 'y' else False
        list_ge = ((i, self.__uc[i]) for i in sorted(self.__uc, key=sort_func.get(sort_key, None), reverse=sort_rev))
        out_format1(list_ge, [], None, None)

    def exit(self, fp_str=''):
        """
        因为系统启动默认会从上一次保存位置加载配置文件，所以
        当输入的路径缺省、输入的路径不存在时、或者输入的路径和上一次保存的路径相同时，直接将文件保存到上一次保存位置self.__save_dir，无须考虑合并
        否则，判断路径是否存在，若存在且以.json结尾，提示用户确认是否覆盖；若存在但不以.json结尾，则依然保存值上一次保存位置
        若路径上文件不存在，则确保路径的后缀名为.json。保存该数据。
        """
        save_uc = self.__uc
        p = Path(fp_str)
        # 当输入的路径非空，且路径存在，并且是该路径和上一次保存路径不是相同路径时
        if fp_str != '' and p.exists() and p.resolve() != Path(self.__save_dir).resolve():
            if p.suffix == '.json':
                info = input('  warning: 指定路径文件已存在(yes: 覆盖(覆盖后原文件无法找回) || 其他:取消覆盖，数据将保存至默认位置)>>>')
                info = info.strip(', :')
                if info == 'yes':
                    self.__save_dir = fp_str
            else:
                print('  warning: 不规范路径(不是json文件，数据将保存至默认位置)')
        elif fp_str != '' and not p.exists():
            if p.suffix == '.json':
                self.__save_dir = fp_str
            else:
                self.__save_dir = p.stem+'.json'

        with open(self.__save_dir, 'w') as f:
            json.dump(save_uc, f)
        time_str = self.__pwd_time.strftime('%Y%m%d %H:%M:%S%z')
        save_config = [self.__pw, self.__login_status, self.__pwd_status, time_str]
        with open(self.__config_dir, 'w') as f:
            json.dump(save_config, f)
        print('  tip：数据写入完毕:{}'.format(Path(self.__save_dir).resolve()))

    def load(self, fp_str=''):
        """
        系统启动时，默认会从上一次保存位置加载数据
        路径缺省是，表示导入的路径是上一次保存的位置；路径存在时，判断数据格式是否正确；路径不存在时，提示路径错误
        如果当前内存已有数据，提示是否覆盖，更新。
        """
        load_dir = None
        p = Path(fp_str)
        if fp_str == '':
            load_dir = self.__save_dir
        elif p.is_file() and p.suffix == '.json':
            load_dir = fp_str
        else:
            print('  warning：数据加载失败(指定路径 "{}" 文件不存在或者不是json文件)'.format(fp_str))
        if load_dir:
            get_uc = jfr(load_dir)
            num = len(get_uc)
            if not num:
                print('  warning: 从 "{}" 文件获取 0 条有效数据，请检测文件是否正确'.format(fp_str))
            elif self.__uc:                     # 系统当前已经有数据
                info = input('  warning：系统当前已有数据( 请再三确认后操作 cover:替换 || update：更新 || 其他：取消本次导入')
                if info == 'cover':
                    self.__uc = get_uc
                    print('  tip: 成功导入 {} 条数据，原有数据已覆盖'.format(num))
                elif info == 'update':
                    self.__uc = combine(self.__uc, get_uc)
                else:
                    print('  tip:已取消本次导入操作')
            else:                               # 当前self.__uc中没有数据
                self.__uc = get_uc
                print('  tip: 成功导入 {} 条数据'.format(len(self.__uc)))


if __name__ == '__main__':
    cmd_str = ['add', 'update', 'find', 'delete', 'list', 'exit', 'load', 'help']
    um = UserManager()
    um.startup()
    pwd_verify = [True, True, True, True, True, False, True, False]                                    # 命令是否需要密码验证
    input_promote = ['用户详细信息', '用户详细信息', '用户名', '用户名', '排序信息', '保存路径', '加载路径', None]  # 提示信息
    input_check = [dck3, dck3, dck1, dck1, None, None, None, None]                                       # 数据检测函数
    cmd_fn = [um.add, um.update, um.find, um.delete, um.list, um.exit, um.load, None]                    # 输入相对应的命令
    auto_quit = [False, False, False, False, True, True, True, True]                     # 执行完命令后是否，是否停留在当前命令

    data_map = map(lambda v, w, x, y, z: (v, w, x, y, z), pwd_verify, input_promote, input_check, cmd_fn, auto_quit)
    register = dict(zip(cmd_str, data_map))
    while True:
        cmd = input("Command >>> ")
        if cmd not in register:         # 输入命令非法
            print("  warning: 非法命令，请使用：{} ,输入help查看详细".format(' '.join(cmd_str)))
            continue
        op = register[cmd]              # 输入命令合法时，得到操作函数，以及获取数据的方法
        if op[0]:                       # 为True时，表示需要密码验证
            if not um.verify():         # 密码验证失败，则命令无效，要求重新输入命令。
                continue
        if op[1] is None:               # 如果命令不需要数据，说明是help命令
            print(UserManager.__doc__)
            continue
        while True:
            input_time = datetime.datetime.now(tz=time_zone)
            data = inp(cmd, op[1])      # 调用input函数获取数据，提示信息为当前所在命令模式，及提示信息op[0]
            get_delta = (datetime.datetime.now(tz=time_zone)-input_time).total_seconds()
            if op[0] and get_delta > 180:   # 当该命令是需要验证密码时，输入数据超时时，会提示超时并退出当前命令模式;否则可以免验证多次输入数据
                print('  warning: 输入超时，请重新验证密码后再进行操作')
                break
            if cmd != 'exit' and data == 'q!':  # exit命令不能取消输入数据，否则break之后判断命令为cmd就退出系统，造成数据无法保存
                break
            elif op[2] is not None:      # 数据不需要检测
                data = op[2](data)
            op[3](data)                 # 执行命令 op[3]是命令函数， data是数据原
            if op[4] is True:           # 判断操作完是否要退出,如输入add命令，录入了一个用户信息，可以不用再输入add就继续录入下一个用户信息
                break
        if cmd == 'exit':
            print('  bye-bye! 您已成功退出用户信息管理系统！')
            break

# 可以给99分,满分100，为什么扣除1分，是为了怕你骄傲
