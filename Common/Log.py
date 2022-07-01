# @Author: fankang
# @Time: 2022/6/25 16:27

"""
封装log方法

"""
import datetime
import logging
import os

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'debug'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)
    logger.addHandler(MyLog.terminal_handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)


def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


class MyLog:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path+'/Log/log.log'
    err_file = path+'/Log/err.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)

    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    terminal_handler = logging.StreamHandler()

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug(f"[DEBUG {get_current_time()}]:{log_meg}")
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info(f"[INFO {get_current_time()}]:{log_meg}")
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning(f"[WARNING {get_current_time()}]:{log_meg}")
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error(f"[ERROR {get_current_time()}]:{log_meg}")
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.critical(f"[CRITICAL {get_current_time()}]:{log_meg}")
        remove_handler('critical')


if __name__ == "__main__":
    MyLog.debug("This is debug message")
    MyLog.info("This is info message")
    MyLog.warning("This is warning message")
    MyLog.error("This is error message")
    MyLog.critical("This is critical message")

