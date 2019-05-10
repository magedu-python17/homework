import logging
from functools import wraps


def sigleton(cls):
    instance = None
    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper

def getlogger(name,filepath):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handle = logging.FileHandler(filename=filepath)
    fmt = logging.Formatter(fmt='%(asctime)s  %(name)s  %(funcName)s  %(message)s')
    handle.setFormatter(fmt)
    handle.setLevel(logging.INFO)
    logger.addHandler(handle)
    logger.propagate = False
    return logger

