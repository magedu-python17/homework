import asyncio
import requests
import time

now = lambda: time.time()

async def status(url):
    ret = requests.get(url)
    status = 'url -> {} , status -> {}'.format(url,ret.status_code)
    return status

start = now()

tasks = []
for x in ['http://www.baidu.com','http://www.163.com','http://www.qq.com','http://cn.bing.com','http://www.cisco.com']:
    tasks.append(asyncio.ensure_future(status(x)))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())

print('TIME: ', now() - start)

# 你这样有点偷懒了，要用源生的yield