"""
__author__ = 'Administrator'
__mtime__ = '2019/3/13'
# code is far away from bugs with the god animal protecting，I love animals.         
"""

# 本周作业来啦各位小伙伴：3.11-3.24
# http://note.youdao.com/noteshare?id=752ebf731aa0baa56469e8a0648037d8
# 参考这个资料，来实现一个简单的监控 cpu 硬盘  内存等信息的脚本，把这些信息，
# 按固定追加的格式写入到一个文件中：{ip:{'cpu':xxx, 'mem':xxxx, 'disk':xxx, 'time':time.time}}.
# 要求：每个5s写入一次，持续写入一个小时。
# 写入完成后，分析这段数据，并且找出cpu，内存，使用率最高的前5条数据

import psutil
import datetime
import time
import getpass

# 保存文件
def save_file(content,filepath):
    with open(filepath,'a+') as f:
        f.write(content)
        f.close()

# 获取相关信息如下
def get_info_laptop(user,filepath):
    # 获取硬盘的信息
    disk = {
        'disk-C':int(psutil.disk_usage('C:\\').percent*100),
        'disk-D':int(psutil.disk_usage('D:\\').percent*100),
        'disk-E':int(psutil.disk_usage('E:\\').percent*100),
        'disk-F':int(psutil.disk_usage('F:\\').percent*100),
    }
    # 获取当前时间
    now_time = time.strftime('%Y:%m:%d %H-%M-%S',time.localtime(time.time()))
    # 查看内存相关信
    mem = psutil.virtual_memory()
    # 使用信息字典
    use_info = {user:{'cpu': '{} %'.format(int(psutil.cpu_percent(1))), \
                              'mem': '{} %'.format(int(mem.used/mem.total*100)), \
                              'disk':{
                                  'disk-C':'{} %'.format(int(psutil.disk_usage('C:\\').percent)),
                                  'disk-D':'{} %'.format(int(psutil.disk_usage('D:\\').percent)),
                                  'disk-E':'{} %'.format(int(psutil.disk_usage('E:\\').percent)),
                                  'disk-F':'{} %'.format(int(psutil.disk_usage('F:\\').percent))
                              }, \
                              'time':int(time.time())}}

    #保存文件信息
    save_file(str(use_info),filepath)  #保存当前获取的信息并保存文件中
    print(use_info)  #打印获取当前的信息
    save_file('\n',filepath)

# 程序主函数
def main(filepath,times,use,continues=5):
    while times > 0:
        get_info_laptop(use,filepath)
        times-=continues
        time.sleep(continues) #停顿5秒钟


if __name__ == '__main__':
    filepath = 'D:\\laptop_log.txt'
    # 获取当前登录的用户名
    use = getpass.getuser()
    # 持续登录时间
    times = 1*60*60
    main(filepath,times,use)


# 逻辑上看着没有问题啥问题的
