import socket
import threading
import selectors
from queue import Queue
from .config import logger, SERVER_IP, SERVER_PORT
import json
from .service import store_agent_base, store_agent_disk, store_state_base, store_state_disk


class FtpServer:
    def __init__(self):
        self.__addr = (SERVER_IP, SERVER_PORT)
        self.sock = socket.socket()
        self.selector = selectors.DefaultSelector()
        self.event = threading.Event()
        self.q = Queue()

    def serve_forever(self):
        try:
            self.sock.bind(self.__addr)
        except OSError as e:
            self.sock.close()
            logger.error('{} Port occupied, Server quit! {}'.format(self.__addr, e))
            raise
        self.sock.listen(1)
        self.sock.setblocking(False)
        self.selector.register(self.sock, selectors.EVENT_READ, self.accept)
        threading.Thread(target=self.select, name='selector').start()
        threading.Thread(target=self.store, name='sql_store').start()
        logger.info('Server start succeed...')

    def select(self):
        while not self.event.is_set():
            events = self.selector.select()
            for key, mask in events:
                if callable(key.data):
                    callback = key.data
                    callback(key.fileobj, mask)
                else:
                    callback = key.data[0]
                    callback(key, mask)

    def accept(self, sock: socket.socket, mask):
        new_sock, client_addr = sock.accept()
        new_sock.setblocking(False)
        logger.info('client: {} connect'.format(client_addr))
        self.selector.register(new_sock, selectors.EVENT_READ, (self.recv, client_addr))

    def recv(self, key: selectors.SelectorKey, mask):
        if not self.event.is_set():
            new_sock = key.fileobj
            client_addr = key.data[1]
            try:
                data = new_sock.recv(1024)
            except ConnectionResetError:                    # 客户端非正常退出
                logger.info('client: {} quit unusual')
                self._connect_clear(new_sock, client_addr)
                return
            except Exception as e:
                logger.warning(e)
                return
            if data == b'' or data == b'quit':              # 客户端主动发送quit断开
                self._connect_clear(new_sock, client_addr)
                return
            info = json.loads(data.decode())
            info['ip'] = client_addr[0]
            self.q.put(info)

    def store(self):
        while not self.event.is_set():
            info = self.q.get()
            if info is None:                                # 整个服务终止
                continue
            print(info)
            self._store_handle(info)

    @classmethod
    def _store_handle(cls, info):
        ip = info['ip']
        date = info['date']
        hd = (
            ('ab', store_agent_base),
            ('ad', store_agent_disk),
            ('sb', store_state_base),
            ('sd', store_state_disk)
        )                                                   # 注意存储是有顺序的，优先级从高到低： 'ab', 'ad', 'sb', 'sd'
        print('{:20}{}'.format('=======store_handler:', info))
        for key, func in hd:
            value = info.get(key, None)
            if value is not None:
                func(ip, value, date)
                print('{:20}{}{}'.format('=======store_key_value', key, value))

    def _connect_clear(self, sock: socket.socket, client_addr):
        logger.info('client: ip={} quit, begin to clean'.format(client_addr))
        self.selector.unregister(sock)
        self.event.wait(5)
        sock.close()

    def close(self):
        self.event.set()
        self.q.put(None)
        file_objs = []
        for fd, key in self.selector.get_map().items():
            file_objs.append(fd)
        for file_obj in file_objs:
            self.selector.unregister(file_obj)
        self.selector.close()
        self.sock.close()
        logger.info('Server closed successful...')
