import socket
import threading
import logging
from pathlib import Path
from queue import Queue

FORMAT='%(asctime)s    %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

class Ftpcilent:
    def __init__(self, raddr='127.0.0.1', port=9999):
        self.addr = (raddr, port)
        self.sock = socket.socket()
        self.event = threading.Event()
        self.queue = Queue()
        self.dir = self.makedir()

    def makedir(self):
        path = Path('./recvfile')
        path.mkdir(exist_ok=True)
        return path

    def start(self):
        self.sock.connect(self.addr)
        logging.info('已经连接到主机')
        # threading.Thread(target=self.recv, name='CilentRecv').start()

    def recv(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024).decode('GBK')
            except Exception as e:
                logging.info(e)
                break
            logging.info(data)

    def stop(self):
        self.sock.close()
        self.event.wait(3)
        self.event.set()
        logging.info('client stop')

    def run(self):
        self.start()
        while not self.event.is_set():
            cmd = input('>>>')
            if cmd == 'list':
                self.sock.send(cmd.encode('GBK'))
                logging.info(self.sock.recv(1024).decode('GBK'))
            elif cmd.startswith('upload'):
                *_, filepath = cmd.partition(' ')
                path = Path(filepath)
                self.sock.send(cmd.encode('GBK'))
                try:
                    with open('{}'.format(path), 'rb') as f:
                        fileinfo = f.read()
                        filelength = len(fileinfo)
                    self.sock.send(str(filelength).encode('GBK'))
                    self.sock.recv(1024)
                    logging.info(str(filelength))
                    width = 0
                    while True:
                        width = self.sock.send(fileinfo[width:])
                        if not width:
                            break

                except FileNotFoundError as e:
                    logging.info(e)

            elif cmd.startswith('download'):
                self.sock.send(cmd.encode('GBK')) #发送要下载的是哪个文件
                *_, filename = cmd.rpartition(' ') #download XXX.txt
                self.sock.setblocking(True)
                length = int(self.sock.recv(1024))
                print(filename)
                self.sock.send('ack'.encode('GBK'))
                remote_filedata = b''
                while True:
                    info = self.sock.recv(1024)
                    remote_filedata += info
                    if len(remote_filedata) >= length:
                        break
                with open(r'recvfileclient\{}'.format(filename, ), 'wb') as f:
                    f.write(remote_filedata)
                print('download done')

            elif cmd.startswith('quit'):
                self.stop()

fc = Ftpcilent()
fc.run()

