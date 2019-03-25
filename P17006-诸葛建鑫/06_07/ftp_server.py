#! /usr/bin/env python
# author = zhuge
# date = 2019/2/22 9:18
# filename = 06_ftp_P17006_v1.py
import socket
import threading
import logging
import selectors
import json
from queue import Queue
from pathlib import Path
import datetime
import configparser
import sys
lock = threading.Lock()
FORMAT = '%(asctime)s %(threadName)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

# 系统配置信息
ip = '192.168.0.151'
port = 10021
read_length = 4096
config = configparser.ConfigParser()
config.read('./user.cfg')
home = config.defaults()['home']
HOME = Path(home)
USER = {}
for section in config.sections():
    if config.has_option(section, 'passwd'):
        pw = config.get(section, 'passwd')
    else:
        logging.info('Wrong format in config file: ./user.cfg')
        sys.exit(1)
    if config.has_option(section, 'home'):
        hm = config.get(section, 'home')
    else:
        hm = home
    USER[section] = [pw, hm]
print(USER)


class FtpServerConnect:
    def __init__(self, addr):
        self.addr = addr
        self.sock = socket.socket()
        self.event = threading.Event()
        self.selector = selectors.DefaultSelector()

    def start(self):
        try:
            self.sock.bind(self.addr)
        except OSError as ose:
            self.sock.close()
            logging.error(ose)
            raise
        self.sock.listen(1)
        self.sock.setblocking(False)
        self.selector.register(self.sock, selectors.EVENT_READ, self.accept)
        threading.Thread(target=self.select, name='selector').start()

    def select(self):
        while not self.event.is_set():
            events = self.selector.select()         # 阻塞
            for key, mask in events:
                if callable(key.data):
                    callback = key.data
                    callback(key.fileobj, mask)
                else:
                    callback = key.data[0]
                    callback(key, mask)

    def accept(self, sock: socket.socket, mask):
        new_sock, caddr = sock.accept()
        new_sock.setblocking(False)
        q = Queue()
        sh = SessionHandle(new_sock, q)             # 只要有连接，就实例化一个sh对象，使用该对象的start()函数处理
        threading.Thread(target=sh.start, name='client-{}'.format(caddr)).start()
        logging.info('客户端{}已连接'.format(caddr))
        self.selector.register(new_sock, selectors.EVENT_READ, (self.receive, q, sh))

    def receive(self, key: selectors.SelectorKey, mask):
        if not self.event.is_set():
            new_sock = key.fileobj
            q = key.data[1]                 # 每个链接单独的q
            sh = key.data[2]
            caddr = new_sock.getpeername()
            data = new_sock.recv(read_length)
            if data == b'' or data == b'quit':
                logging.info('客户端{}已断开连接'.format(caddr))
                self.selector.unregister(new_sock)
                q.put(b'')
                self.event.wait(2)
                new_sock.close()
                del sh
                return
            q.put(data)

    def stop(self):
        self.event.set()
        fobjs = []
        for fd, key in self.selector.get_map().items:
            fobjs.append(key.fileobj)
        for fobj in fobjs:
            self.selector.unregister(fobj)
        self.selector.close()
        self.sock.close()


class SessionHandle:
    def __init__(self, sock: socket.socket, q: Queue):
        self.sock = sock
        self.client = sock.getpeername()
        self.q = q
        self.event = threading.Event()
        self.home = HOME
        self.current = self.home

    @classmethod
    def pretreatment_head(cls, head: dict):
        msg_h = json.dumps(head).encode()       # 将head即字典对象转化为字符串，在使用str.encode()变为bytes
        len_head = len(msg_h)+2                 # 头部长度，size占两个bytes
        msg_s = len_head.to_bytes(2, 'big')     # 头部的size长度
        msg = msg_s+msg_h
        return msg

    def start(self):
        while not self.event.is_set():
            data = self.q.get()
            if data == b'':                     # 客户端断开，则客户端对应的sh线程也需要结束了，执行清理操作
                break
            size = int.from_bytes(data[0:2], 'big')
            msg_h = data[2:]
            count = (size-1)//read_length+1
            for i in range(1, count):
                try:
                    data = self.q.get(timeout=30)
                except BaseException as be:
                    logging.info(be)
                    msg = self.pretreatment_head({'s': 421, 'p': 'Connection timed out'})
                    self.sock.send(msg)
                    return False
                msg_h += data
            head = json.loads(msg_h.decode())
            getattr(self, head['c'])(head)

    def auth(self, head):
        info = json.loads(head['o'])
        u = info['u']
        p = info['pw']
        flag = False
        if u in USER:
            if p == USER[u][0]:
                new_head = {'s': 226, 'p': 'Authentication pass'}
                flag = True
            else:
                new_head = {'s': 499, 'p': 'Bad password, connection broken'}
        else:
            new_head = {'s': 498, 'p': 'Bad user, connection broken'}
        msg = self.pretreatment_head(new_head)
        self.sock.send(msg)

    def dir_judge(self, p: Path):               # 验证新路径是否超过当前用户家目录
        flag = True
        try:
            tmp = p.resolve().relative_to(self.home.resolve())
        except ValueError:
            flag = False
        if flag:
            ret = {'s': 226, 'p': "succeed"}
        else:
            ret = {'s': 420, 'p': "Permission denied: path out of user's home"}
        return ret

    def cd(self, head: dict):
        ps = head['o']
        new_current = self.current/ps
        if not new_current.exists():
            new_head = {'s': 410, 'p': "The path does't exist!"}
        elif new_current.is_file():
            new_head = {'s': 411, 'p': "Path is not a directory"}
        else:
            new_head = self.dir_judge(new_current)
        if new_head['s'] == 226:
            self.current = self.current/ps
        msg = self.pretreatment_head(new_head)
        self.sock.send(msg)

    def ls(self, head: dict):
        """ ls ./hello/ """
        def _ls(fp: Path):
            if fp.is_dir():
                ty = 'd'
            elif fp.is_block_device():
                ty = 'b'
            elif fp.is_char_device():
                ty = 'c'
            elif fp.is_socket():
                ty = 's'
            elif fp.is_symlink():
                ty = 'l'
            else:
                ty = '-'
            lst1 = ['r', 'w', 'x']
            bit = 0x100
            stat = fp.stat()
            mode_num = stat.st_mode
            mode = ''
            for i in range(9):
                if mode_num & bit:
                    mode += lst1[i % 3]
                else:
                    mode += '-'
                bit = bit >> 1
            m = '{}{}'.format(ty, mode)
            at = datetime.datetime.fromtimestamp(stat.st_atime).strftime('%b %d %H:%M')
            n = fp.name
            return m, stat.st_nlink, stat.st_uid, stat.st_gid, stat.st_size, at, n

        prompt = '\n'
        new_head = {}
        p = self.current
        flag = True                         # 标记要查询的是否是一个目录
        if head.get('o', None):             # 判断ls是否携带路径，如果有路径，则
            ps = head['o']
            p = self.current/ps
            if not p.exists():
                new_head = {'s': 410, 'p': "The path {} does't exist!".format(ps)}
                flag = False
            elif p.is_file():
                flag = False
                p_parent = p.parent
                ret = self.dir_judge(p_parent)
                if ret['s'] != 226:
                    new_head = ret
                else:
                    t = _ls(p)
                    prompt += ''.join(t)
                    new_head = {'s': 226, 'p': prompt}
        if flag:
            ret = self.dir_judge(p)
            if ret['s'] != 226:
                new_head = ret
            else:
                info = []
                for sub_ps in p.iterdir():
                    t = _ls(sub_ps)
                    info.append(t)
                size = (t[4] for t in info)
                ss = sorted(size, reverse=True)
                ms = len(str(ss[0]))
                for t in info:
                    prompt += '{0} {1} {2} {3} {4:>{7}} {5} {6}\n'.format(*t, ms)
                new_head = {'s': 226, 'p': prompt.rstrip()}
        msg = self.pretreatment_head(new_head)
        self.sock.send(msg)
        return

    def put(self, head: dict):                  # 客户端上传文件，文件或目录都将保存ftp服务器当前目录self.current。
        # 上传文件或目录时，如果服务器同名路径下已经有文件或目录，则取消该文件上传
        options = head['o']
        file_lst = []
        prompt = ''
        new_options = []
        for ps, size in options:
            pn = Path(ps).name
            new_p = self.current/pn
            if new_p.exists():
                prompt += '{} exists in server, ignore this path\n'.format(ps)
                continue
            if isinstance(size, list):
                new_p.mkdir()
                for sub_ps, sub_size in size:
                    if sub_size == '':
                        (new_p/sub_ps).mkdir()
                        continue
                    lsub_ps = str(new_p/sub_ps)             # 本地服务器写入的路径是本地的绝对路径
                    rsub_ps = '{}/{}'.format(ps, sub_ps)    # 返回客户端的是客户端原先的路径
                    file_lst.append([lsub_ps, sub_size])
                    new_options.append([rsub_ps, sub_size])
            else:
                file_lst.append([str(new_p), size])
                new_options.append([ps, size])
        new_head = {}
        if new_options:                         # 经处理后有部分文件允许上传
            new_head['c'] = 'upload'
            new_head['o'] = new_options
            if prompt:
                new_head['s'] = 300
                new_head['p'] = prompt
        else:                                   # 要上传的路径服务器上已经存在同名文件
            new_head['s'] = 420
            new_head['p'] = prompt
        msg = self.pretreatment_head(new_head)
        self.sock.send(msg)
        for ps, size in file_lst:
            count = (size - 1) // read_length + 1
            with open(ps, 'ab') as f:
                for i in range(count):
                    try:
                        data = self.q.get(timeout=10)
                    except BaseException as be:
                        logging.info(be)
                        logging.error('[ERROR]: 同客户端"{}"连接超时,文件"{}"接收中断'.format(self.client, ps))
                        status = self.pretreatment_head({'s': 421, 'p': 'Connection timed out'})
                        self.sock.send(status)
                        return False
                    f.write(data)

    def get(self, head: dict):
        options = head['o']
        new_options = []
        prompt = '\n'
        file_lst = []
        for ps in options:
            p = self.current/ps
            if not p.exists():
                prompt += '{}: Path not exist\n'.format(ps)
                continue
            elif p.is_dir():
                ret = self.dir_judge(p)
                if ret['s'] != 226:                                     # 判断路径是否超出home目录，如果超出，结果不等于226
                    prompt += '{} :{} \n'.format(ps, ret['p'])
                    continue
                new_options.append([p.name, ''])                        # 通知用户写入目录,如 ['d', '']表示这是一个目录
                for sub_ps in p.iterdir():
                    rsub_ps = '{}/{}'.format(p.name, sub_ps.name)       # 通知用户写入文件，如 ['./d/test.py', 1024]表示文件
                    sub_size = sub_ps.stat().st_size if sub_ps.is_file() else ''
                    new_options.append([rsub_ps, sub_size])
                    if sub_size != '':                                  # 目录下是文件
                        file_lst.append([str(sub_ps), sub_size])
            else:
                p_parent = p.parent
                ret = self.dir_judge(p_parent)
                if ret['s'] != 226:
                    prompt += '{} :{} \n'.format(ps, ret['p'])
                    continue
                size = p.stat().st_size
                new_options.append([p.name, size])
                file_lst.append([str(p), size])
        if not new_options:                                             # 解析结果为空则说明所有请求的路径都无效
            new_head = {'s': 404, 'p': prompt.rstrip()}
        else:
            new_head = {'c': 'write', 'o': new_options}
            if prompt.rstrip():
                new_head['s'] = 301
                new_head['p'] = prompt.rstrip()
        msg = self.pretreatment_head(new_head)
        self.sock.send(msg)
        if file_lst:
            for ps, size in file_lst:                                   # 如果所有路径无效，则file_lst是空列表
                count = (size - 1) // read_length + 1
                with open(ps, 'rb') as f:
                    for i in range(count):
                        data = f.read(read_length)
                        self.sock.send(data)


def main():
    addr = (ip, port)
    fsc = FtpServerConnect(addr)
    fsc.start()


if __name__ == '__main__':
    main()
# 完成的很好了~