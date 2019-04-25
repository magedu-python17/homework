from watcher.agent.config import URL, DATABASE_DEBUG
from watcher.agent.utils import sigleton
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, String, create_engine,ForeignKey, BIGINT, DateTime
from sqlalchemy.orm import relationship, sessionmaker



Base = declarative_base()

class Host(Base):
    __tablename__ = 'host'

    id = Column(Integer, autoincrement=True, primary_key=True)
    hostname = Column(String(45), nullable=False)
    ip = Column(String(45), nullable=False, unique=True)
    cpu_num = Column(Integer, nullable=False)
    men_size = Column(BIGINT, nullable=False)
    disk_size_total = Column(BIGINT, nullable=False)

    def __repr__(self):
        return f'<Host {self.id} {self.ip} {self.hostname} >'
    __str__ = __repr__

class Disk(Base):
    __tablename__ = 'disk'

    id = Column(Integer, autoincrement=True, primary_key=True)
    partition  = Column(String(45), nullable=False)
    size = Column(BIGINT, nullable=False)
    deleted = Column(Boolean, nullable=False, default=0)
    host_id = Column(Integer, ForeignKey('host.id'), nullable=False)

    host = relationship('Host')
    disk_state = relationship('Disk_state', uselist=False)

    def __repr__(self):
        return f'<Disk {self.id}  {self.host_id} {self.partition} >'

    __str__ = __repr__

class Disk_state(Base):

    __tablename__ = 'disk_state'

    id = Column(Integer, autoincrement=True, primary_key=True)
    size_percent = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    disk_id = Column(Integer, ForeignKey('disk.id'), nullable=False)


    disk = relationship('Disk')

    def __repr__(self):
        return f'<Disk_state {self.id}  {self.disk_id} {self.size_percent} >'

    __str__ = __repr__


class Cm_state(Base):

    __tablename__ = 'cm_state'

    id = Column(Integer, autoincrement=True, primary_key=True)
    men_percent = Column(Integer, nullable=False)
    cpu_percent = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    host_id = Column(Integer, ForeignKey('host.id'), nullable=False)

    host = relationship('Host')

    def __repr__(self):
        return f'<Cm_state {self.id}  {self.host_id} {self.cpu_percent} {self.men_percent}>'

    __str__ = __repr__

@sigleton
class Database:

    def __init__(self, URL, **kwargs):
        self._engine = create_engine(URL, **kwargs)
        self._session = sessionmaker(bind=self._engine)()

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine

    def create_all(self):
        Base.metadata.create_all(self._engine)

    def drop_all(self):
        Base.metadata.drop_all(self._engine)

db = Database(URL, echo=DATABASE_DEBUG)


