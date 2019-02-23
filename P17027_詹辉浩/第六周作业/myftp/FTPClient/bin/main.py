import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.getcwd())))
from core import ftp_client


if __name__ == '__main__':
    ftp_client.main()
