import logging.config
import logging


def get_log():
    con_log = '../config/log.conf'
    logging.config.fileConfig(con_log)
    log = logging.getLogger()
    return log