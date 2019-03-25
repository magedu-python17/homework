import psutil
import datetime
import time
import socket
import fcntl
import struct
import threading

class SystemMonitor():

    def __init__(self):#初始化数据
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.cpumemdisk = []

    def get_ip_address(self, ifname):#获取IP
        return socket.inet_ntoa(fcntl.ioctl(
            self.s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])


    def get_data(self):#获取数据

        cpu = psutil.cpu_percent(interval=1)#获取cpu
        mem = psutil.virtual_memory()#获取内存
        muc = mem.used/mem.total#获取内存使用率
        disk = psutil.disk_usage('/')#获取磁盘
        duc = disk.used/disk.total#获取磁盘使用率
        ctime = "{:%Y/%m/%d %H:%M:%S}".format(datetime.datetime.now())#获取时间
        return [cpu, muc, duc, ctime]

    def wdata(self):#写入数据
        count = 0
        while True:
            ip = self.get_ip_address(b'eth0')
            data = self.get_data()
            cpu, muc, duc, ctime = data
            self.cpumemdisk.append([ip, cpu, muc, duc, ctime])
            systemdata = "{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc ,ctime, '}', '}')
            with open('/home/python/platu/projects/homework/log', 'a') as f:#写数据
                f.writelines(systemdata+'\n')
            time.sleep(5)#5S写一次
            count += 5
            if count == 3600:#一个小时
                command = input('please input cpu|mem|disk')
                if command == 'cpu':#按cpu排序获取前5
                  for ip,cpu,muc,duc, ctime in  sorted(self.cpumemdisk, key=lambda v: v[1], reverse=True)[:5]:
                      print( "{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc ,ctime, '}', '}'))

                elif command == 'mem':#按mem排序获取前5
                    for ip, cpu, muc, duc, ctime in sorted(self.cpumemdisk, key=lambda v: v[2], reverse=True)[:5]:
                        print("{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc, ctime, '}', '}'))

                elif command == 'disk':#按disk排序获取前5
                    for ip, cpu, muc, duc, ctime in sorted(self.cpumemdisk, key=lambda v: v[3], reverse=True)[:5]:
                        print("{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc, ctime, '}', '}'))

                else:
                    print('input error')
                break


a = SystemMonitor()
if __name__ == '__main__':
    a.wdata()
