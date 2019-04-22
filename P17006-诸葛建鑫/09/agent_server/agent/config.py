from pathlib import Path
import logging

# SERVER_IP 要连接的服务端ip、端口信息
SERVER_IP = '127.0.0.1'
SERVER_PORT = 10021


# LOG CONFIG
BASEDIR = Path(__file__).parent
LOG_PATH = BASEDIR/'monitor_client.log'
FORMAT = '%(asctime)s %(levelname)s %(message)s'
# logging.basicConfig(format=FORMAT, datefmt='%Y/%m/%d %I:%M:%S', level=logging.INFO, filename=LOG_PATH)
logging.basicConfig(format=FORMAT, datefmt='%Y/%m/%d %I:%M:%S', level=logging.INFO)
logger = logging.getLogger()

# 客户端接收来自服务端的数据读取的缓冲区大小
READ_LENGTH = 1024

# 监控时间间隔
INTERVAL = 5

# 服务运行状态
STATE_RUNNING = 0
STATE_FAILED = 1
STATE_PENDING = 2

# config 的配置文件，考虑用.ini的形式来试试