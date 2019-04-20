import psutil
import threading
import datetime
from queue import Queue
import json
from .config import STATE_RUNNING, STATE_FAILED, STATE_PENDING, INTERVAL
from .ftpclient import FtpClient


class Monitor:
    def __init__(self, tz: int=8):
        self.q = Queue()
        self.qh = Queue()
        self.event = threading.Event()
        self.fc = self._fc_init()
        self.interval = INTERVAL
        tz = tz if tz < 24 else tz % 24
        self.__tz = datetime.timezone(datetime.timedelta(hours=tz))

        self.__pre = {}
        # 考虑到磁盘变化一般都是渐进式，像cpu和内存才比较关心超过阈值的时间
        self.__comparison = {'sb': [5, 60], 'sd': [1, None], 'ab': [1, None], 'ad': [1, None]}
        self.__sys_check = True

    def _fc_init(self):                 # ftp连接建立
        count = 0
        while True:
            fc = FtpClient(self.q)
            fc.start()
            self.event.wait(1)
            if fc.state == STATE_RUNNING:
                return fc
            else:
                count += 1
            if count > 3:
                self.stop()
                raise TypeError('Connect init failed')

    def sys_check_set(self):
        self.__sys_check = True

    @classmethod
    def _system_resource(cls):          # 系统资源，基本不变，很少需要更新，内存容量已MB为单位，磁盘大小以GB为单位
        cpu_count = psutil.cpu_count()
        mem_size = psutil.virtual_memory().total >> 20
        disk_partition = [dp.mountpoint for dp in psutil.disk_partitions()]
        disk_per_size = {}
        disk_total_size = 0
        for path in disk_partition:
            dp_size = psutil.disk_usage(path).total >> 30
            disk_per_size[path] = dp_size
            disk_total_size += dp_size
        return {
            'ab': [cpu_count, mem_size, disk_total_size],
            'ad': disk_per_size
        }

    @classmethod
    def _runtime(cls):                 # 系统运行资源
        cpu_percent = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory()
        memory_percent = round((memory.total-memory.free)*100/memory.total, 1)
        disk_partitions = [dp.mountpoint for dp in psutil.disk_partitions()]
        disk_per_percent = {path: psutil.disk_usage(path).percent for path in disk_partitions}
        return {
            'sb': [cpu_percent, memory_percent],
            'sd': disk_per_percent
        }

    def monitor(self):
        while not self.event.is_set():
            if self.fc.state == STATE_PENDING:
                continue
            elif self.fc.state == STATE_FAILED:
                self.event.set()
                break
            now = datetime.datetime.now(self.__tz).timestamp()
            stamp = (int(now)//self.interval+1)*self.interval
            self.event.wait(stamp-now)
            info = self._runtime()
            info['date'] = stamp
            if self.__sys_check:
                sr = self._system_resource()
                info.update(sr)
                self.__sys_check = False
            self.qh.put(info)

    def send_handler(self):                         # 如果前后波动在可接受范围，监控数据数据舍弃，减少不关心数据的提交，
        while not self.event.is_set():
            if self.fc.state == STATE_PENDING:
                continue
            elif self.fc.state == STATE_FAILED:     # ftp服务已经启动失败，就无须self.q.put(b'quit')
                self.event.set()
                break
            data = self.qh.get()
            # with open('monitor.log', 'a') as f:
            #     f.write(json.dumps(data))
            #     f.write('\n')
            if not self.__pre:                      # self.__pre为空，表示客户端刚初始化，直接将数据发送给服务端
                self.__pre = data
                self.q.put(json.dumps(data).encode())
                continue
            send_data = {}
            date = data['date']
            print('{:20}{}'.format('1 monitor data', data))
            print('{:20}{}'.format('2 self.__pre', self.__pre))
            for k, current in data.items():
                if k == 'date':
                    continue
                offset, threshold = self.__comparison[k]
                pre = self.__pre[k]
                ret = self._send_check(pre, current, offset, threshold)
                if ret:
                    send_data[k] = ret
                    print('{:20}{} {}'.format('3 need send:', k, ret))
            if send_data:
                for k, v in send_data.items():
                    if k == 'sd' or k == 'ad':
                        self.__pre[k].update(v)
                        continue
                    self.__pre[k] = v                    # 更新保存的当前数据
                print('{:20}{}'.format('4 self.__pre update', self.__pre))
                send_data['date'] = date
                print('{:20}{}'.format('2 send_data', send_data))
                self.q.put(json.dumps(send_data).encode())
            print('\n')

    @classmethod
    def _send_check(cls, pre, current, offset, threshold=None):  # 如果当前值current超过阈值,或者和保存的值pre差值超过偏移量offset，都要发送数据
        if isinstance(current, (list, tuple)):          # 对于列表，只要超出阈值和超出偏移量任意一项满足，该数据要被发送出去
            for i, v in enumerate(current):
                if threshold and v > threshold:
                    return current
                d = v - pre[i] if v >= pre[i] else pre[i] - v
                if d > offset:
                    return current
        elif isinstance(current, dict):                 # 对于字典，是字典的元素满足一项，就会被添加到待发送字典中
            ret = {}
            for i, v in current.items():
                if threshold and v > threshold:
                    ret[i] = v
                    continue
                d = v-pre[i] if v >= pre[i] else pre[i]-v
                if d > offset:
                    ret[i] = v
            return ret
        else:                                           # 对本例，current要么是列表，要么是字典，如下多余的
            if threshold and current > threshold:
                return current
            d = current-pre
            if d > offset:
                return current

    def start(self):
        threading.Thread(target=self.monitor, name='monitor').start()
        threading.Thread(target=self.send_handler, name='submit-handler').start()

    def stop(self):
        self.event.set()
        self.q.put(b'quit')
