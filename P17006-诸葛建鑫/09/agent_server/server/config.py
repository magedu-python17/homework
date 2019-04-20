from pathlib import Path
import logging

# MYSQL config
USERNAME = 'root'
PASSWORD = '1123zhuge'
HOST = '192.168.11.126'
PORT = '3306'
DATABASE = 'monitor'

DATABASE_DEBUG = True

URL = 'mysql+pymysql://{}:{}@{}:{}/{}?{}'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE, 'charset=utf8')


# SERVER_IP 服务端ip, port端口配置信息
SERVER_IP = '0.0.0.0'
SERVER_PORT = 10021


# LOG CONFIG
BASEDIR = Path(__file__).parent
LOG_PATH = BASEDIR/'monitor_server.log'
FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
DATAFMT = '%Y/%m/%d %H:%M:%S'
logger = logging.getLogger('monitorserver')
logger.setLevel(logging.INFO)
fmt = logging.Formatter(FORMAT, DATAFMT)
h1 = logging.StreamHandler()
h1.setFormatter(fmt)
logger.addHandler(h1)

