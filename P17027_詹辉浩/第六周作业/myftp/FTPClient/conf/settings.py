import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080
IPADDR = (SERVER_IP, SERVER_PORT)
CODE_MODE = 'utf-8'
BASE_DIR = os.path.abspath(os.path.dirname(os.getcwd()))
UPLOAD_DIR = os.path.join(BASE_DIR, 'upload_dir')

STATUS_CODE = {
    '200': 'OK!',
    '201': 'username has registered, pls re choice a username, or use password to login.',
    '300': 'File Exists, but not completely',
    '301': 'File Exists Completely!',
    '302': 'Ready to recieve file!',
    '401': 'login failed! username or password incorrect',
    '403': 'forbiden',
    '404': 'No Such directory',
    '405': 'Create dir failed, pls check your path is correct or not!',
    '500': 'user space over quota',
    '502': 'bad gateway'
}