"""
创建数据库数据及销毁数据库数据
        from server.model import db
        db.drop_all()
        db.create_all()
基本使用：
    启动服务端：
        from server.server import FtpServer
        fs = FtpServer()
        fs.serve_forever()
    关闭服务端：
        fs.close()
"""
from .server import FtpServer
