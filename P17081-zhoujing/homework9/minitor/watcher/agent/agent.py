import psutil
import selectors
from functools import wraps
from zerorpc import Client
from socket import socket
from watcher.agent.model import  Disk, Disk_state, Cm_state, Host, db
from watcher.agent.utils import getlogger
import logging
import psutil
from threading import Thread, Event
import os
import datetime

logger = getlogger(__name__,os.path.abspath(os.path.abspath('./recode.log')))


def transactional(fn):
    @wraps(fn)
    def wrapper(*agr, **kwargs):
        ret = fn(*agr, **kwargs)
        try:
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            logger.error(e)
    return wrapper

class Agent:

    def __init__(self,ip='192.168.11.101', port=9000, runtime=3600, interval=5):
        self.sock = socket()
        self.service = (ip, port)
        self.event = Event()
        self.runtime = runtime
        self.interval = interval

    # @transactional
    def reg(self):
        name = psutil.users()[0].name
        self.sock.connect(self.service)
        ip, _ = self.sock.getsockname()
        self.sock.close()
        self.host = db.session.query(Host).filter(Host.ip==ip).first()
        if not self.host:
            self.host = Host()
            self.host.hostname = name
            self.host.ip = ip
            self.host.men_size = psutil.virtual_memory().total
            self.host.cpu_num = psutil.cpu_count()
            # self.host.disk_size_total = psutil.disk_usage()
            self.host.disk_size_total = 0
            for device in psutil.disk_partitions():
                self.host.disk_size_total += psutil.disk_usage(device.device).total
            db.session.add(self.host)
            try:
                db.session.commit()
            except Exception as e:
                    db.session.rollback()
                    logger.error(e)
            for device in psutil.disk_partitions():
                self.disk = Disk()
                self.disk.partition = device.device.rstrip(':\\')
                self.disk.size = psutil.disk_usage(device.device).total
                self.disk.host_id = self.host.id
                self.disk.deleted = 0
                db.session.add(self.disk)
                try:
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    logger.error(e)
                self.dp = Disk_state(size_percent=psutil.disk_usage(device.device).percent,
                                     date=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))), disk_id=self.disk.id)
                db.session.add(self.dp)
                try:
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    logger.error(e)
        self.disks = db.session.query(Disk.id, Disk.partition).filter(Disk.host_id == self.host.id).all()

    def start(self):
        self.reg()
        Thread(target=self.handle).start()
        start = datetime.datetime.now()
        while not self.event.is_set():
            logging.info('正在监控电脑运行情况')

            runtime = (datetime.datetime.now() - start).total_seconds()
            if runtime > self.runtime:
                self.event.set()
        # query = db.session.query(Host.ip, Cm_state.cpu_percent, Cm_state.men_percent, Cm_state.date)\
        #     .join(Cm_state, Cm_state.host_id==self.host.id)\
        #     .filter(Host.id==self.host.id).\
        #     order_by(Cm_state.men_percent.desc())\
        #     .order_by(Cm_state.cpu_percent.desc())\
        #     .limit(5)
        self.event.wait(10)
        # TODO 查回来要干嘛？

    def handle(self):

        while not self.event.is_set():

            cm_state = Cm_state()
            cm_state.cpu_percent = int(psutil.cpu_percent())
            cm_state.men_percent = psutil.virtual_memory().percent
            cm_state.date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
            cm_state.host_id = self.host.id
            db.session.add(cm_state)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logger.error(e)
            for disk in self.disks:
                disk_state = Disk_state()
                disk_state.disk_id = disk.id
                disk_state.size_percent = psutil.disk_usage(disk.partition+':').percent
                disk_state.date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
                db.session.add(disk_state)

                try:
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    logger.error(e)
            self.event.wait(self.interval)

    def end(self):
        self.event.set()



Agent().start()










