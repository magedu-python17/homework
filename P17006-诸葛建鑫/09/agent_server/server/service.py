from functools import wraps
from .model import db, AgentBase, AgentDisk, StateBase, StateDisk


def transactional(fn):
    @wraps(fn)
    def _transactional(*args, **kwargs):
        ret = fn(*args, **kwargs)
        try:
            db.session.commit()
            return ret
        except Exception as e:
            print(e)
            db.session.rollback()
    return _transactional


@transactional
def store_agent_base(ip: str, abs: list, date=None):
    q = db.session.query(AgentBase).filter(AgentBase.ip == ip).first()
    if q:                    # 如果已经有记录，则修改
        ab = q
    else:
        ab = AgentBase()     # 没有记录则增加
    ab.ip = ip
    ab.cpu_count = abs[0]
    ab.memory_size = abs[1]
    ab.disk_total_size = abs[2]
    db.session.add(ab)
    return ab


@transactional
def store_agent_disk(ip: str, d: dict, date=None):
    agent_base_id = db.session.query(AgentBase.id).filter(AgentBase.ip == ip).scalar()
    if not agent_base_id:
        return
    ads = db.session.query(AgentDisk).filter(AgentDisk.agentbase_id == agent_base_id).all()
    if ads:                 # 如果查询到已经有记录，标记删除，添加新的磁盘信息
        for ad in ads:
            ad.is_deleted = 1
            db.session.add(ad)
    for dp, size in d.items():
        ad = AgentDisk()
        ad.agentbase_id = agent_base_id
        ad.dp = dp
        ad.size = size
        db.session.add(ad)


@transactional
def store_state_base(ip: str, bs: list, date: int):
    agent_base_id = db.session.query(AgentBase.id).filter(AgentBase.ip == ip).scalar()
    if not agent_base_id:
        return
    sb = StateBase()
    sb.agentbase_id = agent_base_id
    sb.date = date
    sb.cpu_percent = bs[0]
    sb.memory_percent = bs[1]
    db.session.add(sb)


@transactional
def store_state_disk(ip: str, d: dict, date: int):
    agent_base_id = db.session.query(AgentBase.id).filter(AgentBase.ip == ip).scalar()
    qs = db.session.query(AgentDisk).filter((AgentDisk.agentbase_id == agent_base_id) & (AgentDisk.is_deleted == None))
    ads = qs.all()
    for ad in ads:
        if ad.dp not in d.keys():
            continue
        sd = StateDisk()
        sd.agentdisk_id = ad.id
        sd.date = date
        sd.disk_percent = d[ad.dp]
        db.session.add(sd)




