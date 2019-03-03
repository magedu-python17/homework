#! /usr/bin/env python
# author = zhuge
# date = 2019/2/24 19:34
# filename = 06_ftp_client_P17006.py.py

# ########## 注意点 #############
# 文件操作(读取、创建)应当使用二进制模式，保证文件的一致性，因为文本模式下，文件的读写会根据操作系统的不同来自动替换换行符。
# sock.recv(1024)是每次只读取缓冲去1024个字节长度的bytes数据
# sock.send(msg)应该是可以一次性将数据发送完全？
# ##############################
import socket
import threading
import logging
import sys
import argparse
import json
from pathlib import Path
from queue import Queue
import getpass
FORMAT = '%(asctime)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

read_length = 4096
# 命令行指定要连接的FTP服务ip及port信息，ip必须给定，port默认为10021端口
parser = argparse.ArgumentParser(prog='ftp', description='build a ftp connection')
parser.add_argument('ip', help='the ip address of ftp server to connect')
parser.add_argument('port', nargs='?', default='10021', help='the port of ftp server, default: 10021')


class FtpClientConnect:
    def __init__(self, saddr):
        self.saddr = saddr
        self.sock = socket.socket()
        self.event = threading.Event()
        self.q = Queue()

    def start(self):
        try:
            self.sock.connect(self.saddr)
        except ConnectionRefusedError:
            logging.error('(error) client quit: server {} refused, please check!'.format(self.saddr))
            sys.exit(1)
        threading.Thread(target=self.receive, name='receive').start()

    def receive(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(read_length)          # 每次读取指定长度4096的内容
            except ConnectionResetError:
                logging.info('与服务器中断连接')
                self.q.put(b'')                             # 给SessionHandle实例发送通知，告知服务器断开连接
                self.stop()
                break
            self.q.put(data)

    def send(self, msg: bytes):
        if not self.event.is_set():
            self.sock.send(msg)
        else:
            logging.info('connecting is broken, reconnect before send data!')

    def stop(self):
        self.event.set()
        self.sock.close()


class SessionHandle:
    """
    协议内容： 命令头部格式： size + 字典
        客户端先发送命令，待服务器校验通过后会返回命令，按照返回的命令执行操作
        命令报文格式：
                size:    固定2个字节（0~64k）,单位是B，即最大命令报文长度64KB, 报文长度，单位主要是便于接收方明白需要从queque中读取多少数据
                cmd:     字符串ls等直接通过
            可选：
                options: 命令要执行的参数, 如get ./test.py中的./test.py
                status:  状态码：
                prompt:  提示信息
        文件数据：
            命令通过后直接传输文件数据，不添加头部，因为文件大小以及传输文件的顺序已经在命令报文中说明
            采用二进制模式传输，文件读取mode = 'rb'
            如果get或put的是一个目录，文件的传输顺序按照info中协定的顺序。
    """
    def __init__(self, fcc: FtpClientConnect):
        self.fcc = fcc
        self.send = fcc.send
        self.rq = fcc.q
        self.valid = {'cd', 'ls', 'put', 'get'}                # 有效命令
        self.pre = {'put', 'get'}                                      # 需要预处理的命令
        self.event = threading.Event()

    def auth(self):
        name = input('connect to ftp server {}. username: '.format(self.fcc.saddr))
        pwd = getpass.getpass('Enter password: ')
        info = {'u': name, 'pw': pwd}
        si = json.dumps(info)
        head = {'c': 'auth', 'o': si}
        msg = self.pretreatment_head(head)
        self.send(msg)
        if self.receive() != 'deny':
            self.start()
        else:
            self.send(b'quit')

    def start(self):
        while not self.event.is_set():
            info = input('ftp >>> ')
            if self.input(info) is not False:   # 如果是False,表示用户命令输入不规范
                if self.receive() is False:     # 如果是False,表示服务器主动断开连接
                    break

    @classmethod
    def pretreatment_head(cls, head: dict):     # 报文头部预处理处理函数
        msg_h = json.dumps(head).encode()       # 将head即字典对象转化为字符串，在使用str.encode()变为bytes
        len_head = len(msg_h)+2                 # 头部长度，size占两个bytes
        msg_s = len_head.to_bytes(2, 'big')     # 头部的size长度
        msg = msg_s+msg_h
        return msg

    # ftp输入命令解析（需要预处理的如put函数，反射到对应的方法上进行处理后再发送给服务器；不需要预处理的报文头部处理后发出）
    def input(self, data: str):
        head = {}
        dlt = data.strip().split(maxsplit=1)            # 例如用户输入：'ls ./test ./hello.txt ./nihao.txt'，则命令c='ls', 参数o
        if not dlt or dlt[0] not in self.valid:         # 如果用户直接回车，或者不是有效命令，返回False
            print('valid command: {}'.format('  '.join(self.valid)))
            return False
        head['c'] = dlt[0]
        if dlt[0] in self.pre:                                  # 如果命令需要预处理，如put后的路径，需要预先读取本地对应文件的大小
            if len(dlt) > 1:
                options = dlt[1].strip()
                ret = getattr(self, dlt[0])(options, head)      # 反射技术传递给相应的函数处理。
                return ret
            else:
                print('命令缺少参数')
                return False
        else:
            if len(dlt) > 1:
                head['o'] = dlt[1].strip()
            msg = self.pretreatment_head(head)
            self.send(msg)

    def put(self, options: str, head: dict):           # 如果选项是目录，则遍历目录下的所有
        lst = options.split()
        new_options = []
        for ps in lst:
            p = Path(ps)
            if not p.exists():
                logging.info('指定路径"{}"不存在,已为你忽略该参数'.format(ps))
                continue
            elif p.is_dir():
                value = []
                for sub_ps in p.iterdir():
                    # 如果目录下是文件，则将附加文件的大小，如果目录下还是目录，则大小为空字符串
                    sub_size = sub_ps.stat().st_size if sub_ps.is_file() else ''
                    value.append([sub_ps.name, sub_size])
            else:                                       # 如果该路径是一个文件
                value = p.stat().st_size
            new_options.append([ps, value])
        if not new_options:                             # 如果参数解析的结果是空，表示给定的路径都不存在
            print('无有效上传路径！请核查')
            return False
        head['o'] = new_options
        msg = self.pretreatment_head(head)
        self.send(msg)

    def get(self, options: str, head: dict):           # 预处理，判断本地是否有该文件或目录
        lst = options.split()
        new_options = []
        for ps in lst:
            pn = Path(ps).name
            if Path(pn).exists():
                print('本地当前路径下已存在同名文件或目录：{}'.format(ps))
            else:
                new_options.append(ps)
        if not new_options:
            print('无有效路径，请重新输入')
            return False
        head['o'] = new_options
        msg = self.pretreatment_head(head)
        self.send(msg)

    # ################## 如下是receive 接收服务器命令的执行过程  ###################################
    def receive(self):
        data = self.rq.get()
        if data == b'':
            self.event.set()
            return False                        # 服务器断开与客户端的连接
        size = int.from_bytes(data[0:2], 'big')
        msg_h = data[2:]
        count = (size-1)//read_length+1      # 是左包后不包，即size=4096,说明只需要1个包，4097就需要两个包
        for i in range(1, count):           # 如果命令一个包放不下，需要读取多个包
            try:
                data = self.rq.get(timeout=30)
            except BaseException as be:
                logging.info(be)
                logging.info('从服务器接收数据超时，请重新发送命令')
                return
            msg_h += data
        head = json.loads(msg_h.decode())
        if head.get('s', None):
            if head.get('p', None):             # 如果有提示，则输出提示
                logging.info('{}: {}'.format(head['s'], head['p']))
            status = head['s']
            if 399 < status < 500:
                return 'deny'
        if head.get('c', None):                 # 如果服务器返回的报文头有命令，反射给对应的方法执行，如客户端发送get,服务器会write命令
            getattr(self, head['c'])(head)

    def upload(self, head):  # 与put命令对应，客户端发送put命令，服务端如果通过，则回复upload命令
        options = head['o']
        for ps, size in options:
            count = (size - 1) // read_length + 1  # 用于显示进度条
            degree = count / 10
            level = 1
            with open(ps, 'rb') as f:
                for i in range(count):
                    data = f.read(read_length)
                    self.send(data)
                    if degree <= i < count-1:
                        print('\r{:32} {}    {}'.format('---'*level, str(level * 10) + '%', ps), end='')
                        level += 1
                        degree = degree*level
                    else:                       # i==count-1表示已经接受了count个报文，当前文件数据接收完毕
                        print('\r{:32} {}    {}'.format('---'*10, '100%', ps))
            print('upload ok')

    def write(self, head):                          # 由于在发送get命令之前已经确认本地没有同名文件，因此不需要考虑同名
        options = head['o']
        for ps, size in options:
            if size == '':
                Path(ps).mkdir()
                continue
            count = (size-1)//read_length+1
            degree = count//10
            level = 1
            with open(ps, 'ab') as f:
                for i in range(count):
                    try:
                        data = self.rq.get(timeout=10)
                    except BaseException as be:
                        logging.info(be)
                        logging.error('[error]: 同服务器连接断开，文件{}接收中断'.format(ps))
                        return False
                    f.write(data)
                    if degree <= i < count-1:
                        print('\r{:32} {}    {}'.format('---' * level, str(level * 10) + '%', ps), end='')
                        level += 1
                        degree = degree * level
                    else:
                        print('\r{:32} {}    {}'.format('---' * 10, '100%', ps))

            print('write_ok')


def main():
    args = parser.parse_args()
    addr = (args.ip, int(args.port))
    fcc = FtpClientConnect(addr)
    fcc.start()
    sh = SessionHandle(fcc)
    sh.auth()


if __name__ == '__main__':
    main()







