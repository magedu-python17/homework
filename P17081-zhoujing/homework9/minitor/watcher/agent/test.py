# from watcher.agent.model import *
# import psutil
# for i in range(5):
#     print(psutil.cpu_percent(0.1))
import datetime

s = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
q = datetime.datetime.now().timestamp()
print(s, type(s))
print(q, type(q))
# disks = db.session.query(Disk.id, Disk.partition).filter(Disk.host_id == 1).all()
# for disk in disks:
#     print(disk.id)



