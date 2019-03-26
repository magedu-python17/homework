import psutil
import datetime
import time
import socket
import fcntl
import struct
import threading

class SystemMonitor():

    def __init__(self):#��ʼ������
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.cpumemdisk = []

    def get_ip_address(self, ifname):#��ȡIP
        return socket.inet_ntoa(fcntl.ioctl(
            self.s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])


    def get_data(self):#��ȡ����

        cpu = psutil.cpu_percent(interval=1)#��ȡcpu
        mem = psutil.virtual_memory()#��ȡ�ڴ�
        muc = mem.used/mem.total#��ȡ�ڴ�ʹ����
        disk = psutil.disk_usage('/')#��ȡ����
        duc = disk.used/disk.total#��ȡ����ʹ����
        ctime = "{:%Y/%m/%d %H:%M:%S}".format(datetime.datetime.now())#��ȡʱ��
        return [cpu, muc, duc, ctime]

    def wdata(self):#д������
        count = 0
        while True:
            ip = self.get_ip_address(b'eth0')
            data = self.get_data()
            cpu, muc, duc, ctime = data
            self.cpumemdisk.append([ip, cpu, muc, duc, ctime])
            systemdata = "{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc ,ctime, '}', '}')
            with open('/home/python/platu/projects/homework/log', 'a') as f:#д����
                f.writelines(systemdata+'\n')
            time.sleep(5)#5Sдһ��
            count += 5
            if count == 3600:#һ��Сʱ
                command = input('please input cpu|mem|disk')
                if command == 'cpu':#��cpu�����ȡǰ5
                  for ip,cpu,muc,duc, ctime in  sorted(self.cpumemdisk, key=lambda v: v[1], reverse=True)[:5]:
                      print( "{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc ,ctime, '}', '}'))

                elif command == 'mem':#��mem�����ȡǰ5
                    for ip, cpu, muc, duc, ctime in sorted(self.cpumemdisk, key=lambda v: v[2], reverse=True)[:5]:
                        print("{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc, ctime, '}', '}'))

                elif command == 'disk':#��disk�����ȡǰ5
                    for ip, cpu, muc, duc, ctime in sorted(self.cpumemdisk, key=lambda v: v[3], reverse=True)[:5]:
                        print("{}{}:{}'cpu':{}%, 'mem':{:.2%},'disk':{:.2%}, 'time':{}{}{}".format('{', ip, '{', cpu, muc, duc, ctime, '}', '}'))

                else:
                    print('input error')
                break


a = SystemMonitor()
if __name__ == '__main__':
    a.wdata()
# 能不能同时监控：mem disk cpu 这些，尝试下