import socket
import threading
from queue import Queue
from .config import logger, READ_LENGTH, STATE_PENDING, STATE_FAILED, STATE_RUNNING, SERVER_IP, SERVER_PORT


class FtpClient:
    def __init__(self, q: Queue):
        self.saddr = (SERVER_IP, SERVER_PORT)
        self.sock = socket.socket()
        self.event = threading.Event()
        self.q = q
        self.state = STATE_PENDING

    def start(self):
        try:
            self.sock.connect(self.saddr)
        except ConnectionRefusedError as e:
            self.sock.close()
            logger.error('Client quit! Connecting timeout, check server {}: {}'.format(self.saddr, e))
            self.state = STATE_FAILED
            raise
        logger.info('Connect to Server succeed...')
        threading.Thread(target=self.recv, name='receive-from-server').start()
        threading.Thread(target=self.send, name='send-to-server').start()
        self.state = STATE_RUNNING

    def recv(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(READ_LENGTH)
            except ConnectionError:         # 服务端非正常退出
                logger.info('Server break connection')
                self.clear()
                break
            except Exception as e:
                logger.warning(e)
                break
            if data == b'':     # 如果客户端主动断开，self.sock.recv()会收到大量的b''，此时执行清理，并将b''放入q中通知show_receive结束
                self.clear()
                break
            print(data)

    def send(self):
        while not self.event.is_set():
            msg = self.q.get()
            try:
                self.sock.send(msg)
            except OSError:     # 服务端非正常退出
                logger.error('Connection broken by server')
            if msg == b'quit':
                break

    def clear(self):
        self.state = STATE_FAILED
        self.event.set()
        self.sock.close()
