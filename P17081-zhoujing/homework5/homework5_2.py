import threading
import requests
import asyncio

def status(url):
    ret = requests.get(url)
    status = 'url->{}, status->{}'.format(url, ret.status_code)
    print(status)


@asyncio.coroutine
def run():
    for x in ['http://www.baidu.com', 'http://www.163.com', 'http://www.qq.com']:
        # threading.Thread(target=status, args=(x,), name=x).start()
        status(x)
        yield
@asyncio.coroutine
def run1():
    for x in ['http://www.2345.com', 'http://www.123.com', 'http://www.123.com']:
        # threading.Thread(target=status, args=(x,), name=x).start()
        status(x)
        yield
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks =[run(), run1()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    # run()
