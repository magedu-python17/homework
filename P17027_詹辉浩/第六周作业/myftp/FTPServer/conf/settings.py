import os

IPADDR = ('127.0.0.1', 8080)
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
USER_HOME = os.path.join(BASE_DIR, 'home')
CODE_MODE = 'utf-8'
CONF_DIR = os.path.join(BASE_DIR, 'conf')
AUTH_FILE = os.path.join(CONF_DIR, 'user_settings.ini')
LOG_FILE = os.path.join(BASE_DIR, 'log', 'ftpserver.log')
DISK_QUOTA = 1024 * 1024 * 2

STATUS_CODE = {
    '200': 'OK!',
    '201': 'username has registered, pls re choice a username, or use password to login.',
    '300': 'File already exists, but not completely',
    '301': 'File already exists Completely!',
    '302': 'Ready to recieve file!',
    '401': 'login failed! username or password incorrect',
    '403': 'forbiden',
    '404': 'No Such directory',
    '405': 'Create dir failed, pls check your path is correct or not!',
    '500': 'user space over quota',
    '502': 'bad gateway'
}