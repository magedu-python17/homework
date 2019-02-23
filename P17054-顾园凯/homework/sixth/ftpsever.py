import socket
import threading
from pathlib import Path

class FtpServer:

    def __init__(self, ip='127.0.0.1', port=9999, ftpdirm ='C:/Ftp'):#初始化
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.ftpdirm = ftpdirm
        self.ftppathdir = Path(ftpdirm)

    def start(self):#启动监听
        self.sock.bind(self.addr)#绑定
        self.sock.listen()#监听
        #accept会阻塞主进程，所以开个新线程
        threading.Thread(target=self.accept).start()

    def accept(self):#连接到Ftp
        while True:
            sock, client = self.sock.accept()
            #开新线程
            threading.Thread(target=self.recv, args=(sock,)).start()


    def recv(self, sock):
        while True:
            #获取命令
            cmd = sock.recv(1024).decode()
            if cmd == 'put':
                #获取文件名
                filename = sock.recv(1024).decode()
                #获取文件大小
                filesize = sock.recv(1024).decode()
                filesize = int(filesize)
                sendsize = 0
                #文件路径
                ftpdir = Path.joinpath(self.ftppathdir, filename)
                #上传文件
                with open(ftpdir, 'wb') as f:
                    while sendsize != filesize:
                        data = sock.recv(1024)
                        f.write(data)
                        sendsize += len(data)
                    print('{}已接收'.format(filename))

            if cmd == 'get':
                #获取文件名
                filename = sock.recv(1024).decode()
                threading.Thread(target=self.retuen, args=(filename, sock)).start()

            if cmd == 'ls':
                threading.Thread(target=self.ls, args=(sock,)).start()


    def retuen(self, filename, sock):
        #判断文件是否存在
        if filename in (i.name for i in self.ftppathdir.iterdir()):
            #文件路径
            filepath = self.ftpdirm + '/' + filename
            #文件大小
            ftpdir = Path(filepath)
            filesize = Path.stat(ftpdir).st_size
            # 发送文件的大小
            sock.send(str(filesize).encode())
            #用来判断
            getedsize = 0
            #下载
            with open(ftpdir, 'rb') as f:
                while getedsize != filesize:
                    data = f.read(1024)
                    sock.send(data)
                    getedsize += len(data)
                print('{}已被下载'.format(filename))

        else:
            self.sock.send('file is not exist'.encode())

    def ls(self, sock):
        #文件数量
        filenum = len(list(self.ftppathdir.iterdir()))
        #发送文件数量
        sock.send(str(filenum).encode())
        sendnum = 0
        #发送目录
        while sendnum < filenum:
            for i in self.ftppathdir.iterdir():
                sock.send(str(i.name).encode())
                sendnum += 1

    def stop(self):#停止服务
        self.sock.close()

cs = FtpServer()
cs.start()

