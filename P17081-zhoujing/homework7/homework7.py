import psutil
import socket
import datetime
import threading
import logging
from pathlib import Path


logging.basicConfig(format='%(asctime)s    %(message)s', level=logging.INFO)
class Wacther:
    def __init__(self, path, runtime=3600,interval=5):
        self.ip = self.get_local_ip()
        self.dir = Path(path)
        self.runtime = runtime
        self.interval = interval
        self.event =threading.Event()
        self.info =[]

    def start(self):
        threading.Thread(target=self.handle, args=(self.dir,self.interval)).start()
        start = datetime.datetime.now()

        while not self.event.is_set():
            self.event.wait(10)
            logging.info('正在监控电脑运行情况')
            runtime = (datetime.datetime.now() - start).total_seconds()
            if runtime > self.runtime:
                self.event.set()
        max_info = sorted(self.info, key=lambda x:x[self.ip]['cup_percent'] and x[self.ip]['mem_per'],reverse=True)
        max_use_info = ''
        for info in max_info[:5]:
            max_use_info += str(info) +'\n'

        with open(self.dir,'a',encoding='utf8') as f:
            f.write('\n')
            f.write('使用率最高的5条信息：\\n')
            f.write(max_use_info)

    def stop(self):
        self.event.set()

    def handle(self,path,interval):

        while not self.event.is_set():
            self.event.wait(interval)
            cpu_per = psutil.cpu_percent()
            mem = psutil.virtual_memory()
            men_per = mem.used / mem.total
            disk = psutil.disk_usage('/')
            time = datetime.datetime.now().strftime('%y-%m-%d  %H:%M:%S')

            infomation  = {self.ip:{
                'cup_percent': cpu_per,
                'mem_per': men_per,
                'disk' : disk,
                'time': time
                 }
                           }
            self.info.append(infomation)

            with open(path,'a',encoding='utf8') as f:
                f.write(str(infomation))

    def get_local_ip(self):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('1.1.1.1', 80))
            ip, _ = s.getsockname()
            return ip

        except:pass
        finally:
            s.close()

if __name__ == '__main__':
    w = Wacther('./log.txt')
    w.start()

