import socket
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.getcwd())))
from core.client_handler import ClientHandler


def show_banner(banner_name):
    print("""
 -----------------------------------------------------------
|                     {}
 -----------------------------------------------------------
    """.format(banner_name))

def main():
    main_banner = """
 -----------------------------------------------------------
|>>>             Welcome to Use MyFTP Client             <<<|
|>>>    pls input your option that you want as follow    <<<|
 -----------------------------------------------------------
"""

    print(main_banner)

    start_list = (('登录','login'), ('注册','register'), ('退出','quit'))
    # for index, option in enumerate(start_list, 1):
    #     print(index, option[0])
    #
    # print()

    client = ClientHandler()

    while True:
        for index, option in enumerate(start_list, 1):
            print(index, option[0])

        print()

        try:
            ops = input("|>>>    ").strip()
            ops = int(ops)

            if ops == 3:
                if not client.sock._closed:
                    client.sock.close()
                break

            opreation = start_list[ops - 1][1]
            if hasattr(client, opreation):
                func = getattr(client, opreation)
                show_banner(opreation)
                func()

        except IndexError as e:
            print('[ERROR] wrong options choice!')

