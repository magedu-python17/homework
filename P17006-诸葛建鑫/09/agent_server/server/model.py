from .config import URL, DATABASE_DEBUG
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, ForeignKey
from functools import wraps
engine = create_engine(URL, echo=DATABASE_DEBUG)
Base = declarative_base()


class AgentBase(Base):
    __tablename__ = 'agentbase'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String(48), nullable=True)
    ip = Column(String(15), nullable=False, unique=True)
    cpu_count = Column(Integer, nullable=False, default=1)
    memory_size = Column(Integer, nullable=False)
    disk_total_size = Column(Integer, nullable=False, default=1024)

    def __repr__(self):
        return '<AgentBase id={} ip={}>'.format(self.id, self.ip)

    __str__ = __repr__


class AgentDisk(Base):
    __tablename__ = 'agentdisk'
    id = Column(Integer, primary_key=True, autoincrement=True)
    agentbase_id = Column(Integer, ForeignKey('agentbase.id'), nullable=False)
    dp = Column(String(20), nullable=False)
    size = Column(Integer, nullable=False)
    is_deleted = Column(Integer, nullable=True)

    agentbase = relationship('AgentBase', backref='agentdisk')

    def __repr__(self):
        return '<AgentDisk agent_id={} disk_partition={} size={}>'.format(self.agentbase_id, self.dp, self.size)

    __str__ = __repr__


class StateBase(Base):
    __tablename__ = 'statebase'
    id = Column(Integer, primary_key=True, autoincrement=True)
    agentbase_id = Column(Integer, ForeignKey('agentbase.id'), nullable=False)
    date = Column(Integer, nullable=False)                  # 查询按照时间戳来查找的，设置该冗余字段，较少查询State表
    cpu_percent = Column(Float, nullable=False)
    memory_percent = Column(Float, nullable=False)

    agentbase = relationship('AgentBase')

    def __repr__(self):
        return '<StateBase agent={} cpu={}% mem={}%>'.format(self.agentbase_id, self.cpu_percent, self.memory_percent)

    __str__ = __repr__


class StateDisk(Base):
    __tablename__ = 'statedisk'
    id = Column(Integer, primary_key=True, autoincrement=True)
    agentdisk_id = Column(Integer, ForeignKey('agentdisk.id'), nullable=False)
    date = Column(Integer, nullable=False)
    disk_percent = Column(Float, nullable=False)

    agentdisk = relationship('AgentDisk')

    def __repr__(self):
        return '<StateDisk disk_id={} disk_percent={}%>'.format(self.agentdisk_id, self.disk_percent)

    __str__ = __repr__


def singleton(cls):
    instance = None

    @wraps(cls)
    def _singleton(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return _singleton


@singleton
class Database:
    def __init__(self, url, **kwargs):
        self._engine = create_engine(url, **kwargs)
        self._session = sessionmaker(bind=self._engine)()

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session

    def create_all(self):
        return Base.metadata.create_all(self._engine)

    def drop_all(self):
        return Base.metadata.drop_all(self._engine)


db = Database(URL, echo=DATABASE_DEBUG)
