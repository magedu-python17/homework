import os, sys
import socketserver
import json
from configparser import ConfigParser
from functools import wraps
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from conf import settings


class MyFTPServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.recv_json()

            operation = data.get('operation')
            if hasattr(self, operation):
                func = getattr(self, operation)
                func(data)

    def login(self,data):
        status_code = self.authenticate(data)
        print(status_code)

        self.send_code(status_code)

    def register(self, data):

        if not self.has_registered(data):

            username = data.get('username')
            password = data.get('password')
            home = os.path.join(settings.USER_HOME, username)

            # 为新注册用户创建家目录
            os.mkdir(os.path.join(settings.USER_HOME, username))

            # 为新注册用户新增配置文件
            cfg = ConfigParser()
            cfg.read(settings.AUTH_FILE)

            cfg.add_section(username)
            cfg.set(username, 'username', username)
            cfg.set(username, 'password', password)
            cfg.set(username, 'disk_quota', str(settings.DISK_QUOTA))
            cfg.set(username, 'home', home)

            with open(settings.AUTH_FILE, 'w') as f:
                cfg.write(f)

            self.send_code('200')

        else:
            self.send_code('201')

    def has_registered(self, data):
        username = data.get('username')
        cfg = ConfigParser()
        cfg.read(settings.AUTH_FILE)

        return cfg.has_section(username)

    def authenticate(self, data):
        print(data)
        username = data.get('username')
        password = data.get('password')

        cfg = ConfigParser()
        cfg.read(settings.AUTH_FILE)

        if cfg.has_section(username):
            user = cfg[username]

            if user['password'] == password:
                self.username = username
                self.mainpath = os.path.join(settings.USER_HOME, self.username)
                return '200'
        else:
            return '401'

    def put(self, data):
        file_name = data.get('file_name')
        file_size = data.get('file_size')
        target_path = data.get('target_path')

        print(data)

        # 拼接上传目录的绝对路径
        abs_path = os.path.join(self.mainpath, target_path, file_name)
        print(abs_path)

        # 判断上传文件的状态，是否存在？是否完整
        if os.path.exists(abs_path):
            file_has_size = os.stat(abs_path).st_size

            # 断点续传情况
            if file_has_size < file_size:
                self.send_code('300')
                choice = self.recv_json()

                # 续传
                if choice == 'Y':
                    self.send_json({'file_has_size':str(file_has_size)})
                    self.exec_upload(abs_path, file_size, 'ab', has_received=file_has_size)

                # 不续传，这里用覆盖的方式
                else:
                    self.exec_upload(abs_path, file_size, 'wb')

            # 文件数据完整的情况
            else:
                self.send_code('301')
                return

        else:
            # 文件不存在，新上传的情况
            self.send_code('302')
            if self.exec_upload(abs_path, file_size, 'wb'):
                pass

        # 需要判断用户磁盘配额大小是否足够，不足则提醒用户, TODO

    def exec_upload(self, open_file, file_size, mode, has_received=0):
        with open(open_file, mode) as f:

            while has_received < file_size:
                try:
                    data = self.request.recv(1024)

                except Exception as e:
                    break

                f.write(data)
                has_received += len(data)

        self.send_code('200')
        return True

    def send_json(self, data):
        data = json.dumps(data).encode(settings.CODE_MODE)
        self.request.send(data)

    def recv_json(self):
        data = self.request.recv(1024).strip()
        data = json.loads(data.decode(settings.CODE_MODE))
        return data

    def ls(self, data):
        operation = data.get('operation')
        path = data.get('path','.')

        file_list = os.listdir(self.mainpath)
        file_str = "\n".join(file_list)

        if not len(file_list):
            file_str = "<Empty Dir>"

        self.request.send(file_str.encode(settings.CODE_MODE))

    def cd(self, data):

        target_dir = data.get('target_dir')

        if target_dir == '..':
            parent_dir = os.path.dirname(self.mainpath)
            self.mainpath = parent_dir


        elif target_dir == '.':
            self.mainpath = self.mainpath

        else:
            print(target_dir)
            self.mainpath = os.path.join(self.mainpath, target_dir)

        basename = os.path.basename(self.mainpath)
        print(basename)
        self.send_json({'basename': basename})

    def pwd(self, data):
        self.send_json({'current_dir': self.mainpath})

    def send_code(self, status_code):
        self.request.send(status_code.encode(settings.CODE_MODE))

    def mkdir(self, data):
        dirname = data.get('dirname')
        path = os.path.join(self.mainpath, dirname)

        if not os.path.exists(path):
            if '/' in dirname:
                os.makedirs(path)
            else:
                os.mkdir(path)

            self.send_code('200')

        else:
            self.send_code('405')