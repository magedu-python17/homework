import os, sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(sys.path)
from core.ftp_server import MyFTPServerHandler
from conf import settings
import socketserver


if __name__ == '__main__':
    print('FTP Server running...')
    server = socketserver.ThreadingTCPServer(settings.IPADDR, MyFTPServerHandler)
    server.serve_forever()
