"""
    使用说明：
        m = Monitor()
        m.start()       客户端启动监控，并向服务端发送数据
        m.stop()        客户端关闭监控
    配置信息修改：
        在config.py中修改服务端地址， 监控间隔
"""
from .agent import Monitor

