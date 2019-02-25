import socket
import threading
from pathlib import Path
import time


class ClientServer:

    def __init__(self, ip='127.0.0.1', port=9999):#初始连接
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.sock.connect(self.addr)
        threading.Thread(target=self.send).start()

    def send(self):
        #定义发送
        while True:
            time.sleep(1)
            command = input('>>>')
            #命令判断
            if command[0:3] == 'put' or command[0:3] == 'get':
                print(1)
                cmd, pathfilename = command.split(':', maxsplit=1)
                pathfile_name = Path(pathfilename)
                filename = pathfile_name.name
                self.sock.send(cmd.encode())
                self.sock.send(filename.encode())
                if cmd == 'put':
                    threading.Thread(target=self.sendput, args=(pathfilename, pathfile_name)).start()

                if cmd == 'get':
                    threading.Thread(target=self.sendget, args=(pathfilename,)).start()

            if command == 'ls':
                self.sock.send(command.encode())
                threading.Thread(target=self.sendls).start()
            else:
                print('cmd error')




    def sendput(self, pathfilename, pathfile_name):
        #获取文件大小
        filesize = Path.stat(pathfile_name).st_size
        self.sock.send(str(filesize).encode())
        sendsize = 0
        #传输文件
        with open(pathfilename, 'rb') as f1:
            while sendsize != filesize:
                data = f1.read(1024)
                self.sock.send(data)
                sendsize += len(data)
            print('上传成功')


    def sendls(self):
        #获取文件数量
        filenum = int(self.sock.recv(1024).decode())
        getnum = 0
        while getnum < filenum:
            print(self.sock.recv(1024).decode())
            getnum += 1

    def sendget(self, filemane):
        #获取文件大小
        filesize = int(self.sock.recv(1024))
        getsize = 0
        with open(filemane, 'wb') as f:
            while filesize != getsize:
                data = self.sock.recv(1024)
                f.write(data)
                getsize += len(data)
            print('文件下载成功')


cl = ClientServer()

# 逻辑上没有什么问题，有些细节的地方可以参看下学号 p17027小伙伴的：像进度条，断点续传之类，认证之类的