import socket
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.getcwd())))
from conf import settings
import json


class ClientHandler:

    authcated = False
    logined = False

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance

        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance

    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect(settings.IPADDR)

    def get_status(self):
        status_code = self.sock.recv(1024).decode(settings.CODE_MODE)
        print("{} {}\n".format(status_code, settings.STATUS_CODE[status_code]))
        return status_code

    def login(self):
        username = input('pls input your username: ').strip()
        password = input('pls input your password: ').strip()

        if username is not None and password is not None:
            data = {'username': username, 'password': password, 'operation': 'login'}
            self.send_json(data)

        if self.get_status() == '200':
            self.username = username
            self.current_dir = '/'
            self.authcated = True
            self.logined = True

        if self.authcated:
            while self.logined:
                self.dispatcher()

    def dispatcher(self):
        cmd_list = input("({}@{})[{}]$ ".format(
            self.username,
            settings.SERVER_IP,
            self.current_dir)).split()

        operation = cmd_list[0]
        if hasattr(self, operation):
            func = getattr(self, operation)
            func(cmd_list)

        elif operation == 'exit':
            self.logined = False

        else:
            print('[ERROR] Invalid command')

    def put(self, cmd_list):
        operation, upload_file, target_path = cmd_list
        upload_file = os.path.join(settings.UPLOAD_DIR, upload_file)
        upload_size = os.stat(upload_file).st_size

        data = {
            'file_name':os.path.basename(upload_file),
            'file_size': upload_size,
            'target_path': target_path,
            'operation': operation
            }

        self.send_json(data)
        status_code = self.get_status()

        if status_code == '300':
            # 断点续传的情况
            choice = input("the file exist, is countinue? [Y/n]").strip()

            # 续传
            if choice.upper() == 'Y':
                self.send_json('Y')
                continue_position = int(self.recv_json().get('file_has_size'))
                self.exec_upload(upload_file, upload_size, has_sent=continue_position)

            # 不续传
            else:
                self.send_json('N')
                self.exec_upload(upload_file, upload_size)

        elif status_code == '301':
            # 文件数据完整地保存在server端的情况，不做处理，直接返回
            return

        else:
            # 新上传文件，建立传输的情况
            self.exec_upload(upload_file, upload_size)

    def exec_upload(self, open_file, file_size, mode='rb', has_sent=0):
        with open(open_file, mode) as f:

            f.seek(has_sent)

            while has_sent < file_size:

                data = f.read(1024)
                self.sock.send(data)
                has_sent += len(data)
                self.show_progress(has_sent, file_size)

        self.get_status()

    def register(self):

        while True:
            username = input('register name>>> ')
            password = input('register password>>> ')
            password_ensure = input('ensure password>>> ')

            if username is not None and password is not None and password == password_ensure:
                data = {'username': username, 'password': password, 'operation': 'register'}
                self.send_json(data)
                if self.get_status() == '200':
                    break

            else:
                print('incorrect register information in your input, pls re input...')

    def send_json(self, send_data):
        send_data = json.dumps(send_data).encode(settings.CODE_MODE)
        self.sock.send(send_data)

    def recv_json(self):
        recv_data = self.sock.recv(1024).decode(settings.CODE_MODE)
        recv_data = json.loads(recv_data)
        return recv_data

    # 进度条功能
    def show_progress(self, has_sent, file_size):
        rate = float(has_sent)/float(file_size)
        percentage = int(rate * 100)
        sys.stdout.write("%s%% [%s]\r" % (percentage, '#'*(percentage//3)))
        sys.stdout.flush()
        if has_sent == file_size:
            sys.stdout.write('\n')

    def ls(self, cmd_list):
        self.send_json({'operation': 'ls'})
        data = self.sock.recv(1024).decode(settings.CODE_MODE)
        print(data)

    def cd(self, cmd_list):
        target_dir = cmd_list[1]
        data = {'operation': 'cd', 'target_dir': target_dir}

        self.send_json(data)
        data = self.recv_json()
        self.current_dir = data.get('basename')

        if self.current_dir == self.username:
            self.current_dir = '/'

    def mkdir(self, cmd_list):
        data = {'operation': cmd_list[0], 'dirname': cmd_list[1]}
        self.send_json(data)

        self.get_status()

    def pwd(self, cmd_list):
        self.send_json({'operation': 'pwd'})
        abs_current_dir = self.recv_json().get('current_dir')
        current_dir = os.path.basename(abs_current_dir)
        if current_dir == self.username:
            current_dir = '/'

        print(current_dir)

# ls cd  mkdir pwd 这些能不能写成一个通用的功能？
