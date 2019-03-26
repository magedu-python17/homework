import socket
import threading
import logging
import selectors
from pathlib import Path
FORMAT='%(asctime)s   %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class FtpServer:
    def __init__(self, lip='127.0.0.1', port=9999):
        self.addr = (lip, port)
        self.sock = socket.socket()
        self.sel = selectors.DefaultSelector()
        self.event = threading.Event()
        self.files = {}
        self.dir = self.makedir()

    def makedir(self):
        path = Path('./recvfile')
        path.mkdir(exist_ok=True)
        return path

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        self.sock.setblocking(False)
        self.sel.register(self.sock, selectors.EVENT_READ, data=self.accept)
        threading.Thread(target=self.select, name='accept').start()
        logging.info('Ftp  server start!')

    def select(self):
        while not self.event.is_set():
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj)

    def accept(self,sock):
        conn, laddr =self.sock.accept()
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, data=self.recv)

    def recv(self, sock:socket.socket):
        try:
            data = sock.recv(1024)
        except Exception as e:
            logging.info(e)
            data = b''
        logging.info(data)
        if not data or data == b'quit':
            self.sel.unregister(sock)
            sock.close()
            return
        else:
            if data == b'list':
                msgs = self.dir.iterdir()
                fileinfo=''
                for msg in msgs:
                    fileinfo += msg.name+' '
                sock.send(fileinfo.encode('GBK'))

            elif data.startswith(b'upload'):
                sock.send('start!'.encode('GBK'))
                *_, filepath = data.decode('GBK').rpartition(' ') #写文件路径 客户端直接开始发送数据
                *_ , filename = filepath.rpartition('\\')
                sock.setblocking(True)
                length = int(sock.recv(1024))
                sock.send('ack'.encode('GBK'))

                remote_filedata = b''
                while True:
                    info = sock.recv(1024)
                    remote_filedata += info
                    if len(remote_filedata) >= length:
                        break
                with open(r'recvfile\{}'.format(filename,),'ab') as f:
                    f.write(remote_filedata)
                sock.send('has done'.encode('GBK'))
                sock.setblocking(False)

            elif data.startswith(b'download'):
                *_, filename = data.decode('GBK').partition(' ')
                path = Path('recvfile\{}'.format(filename))
                print(path.absolute())
                with open('{}'.format(path), 'rb') as f:
                    fileinfo = f.read()
                    filelength = len(fileinfo)
                sock.send(str(filelength).encode('GBK'))
                sock.setblocking(True)
                sock.recv(1024)
                logging.info(str(filelength))
                width = 0
                while True:
                    width = sock.send(fileinfo[width:])
                    if not width:
                        break
                sock.setblocking(False)


    def stop(self):
        self.event.set()
        fileobjs = []
        for key in self.sel.get_map().values():
            fileobjs.append(key.fileobj)

        for fileobj in fileobjs:
            self.sel.unregister(fileobj)
            fileobj.close()
        self.sel.close()

ss = FtpServer()
ss.start()
while True:
    cmd = input()
    if cmd == 'q':
        ss.stop()
        break

# 有个更方便的socketserver 你可以看下