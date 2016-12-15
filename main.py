# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import os
import logging
import logging.config
import threading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(os.path.join(BASE_DIR, 'logging.conf'))
logger = logging.getLogger('verbose')


ip = '0.0.0.0'
port = 2071

if __name__ == "__main__":

    from _main import init_server, init_task

    logger.info('Starting Task...')
    task = threading.Thread(target=init_task)
    task.start()

    logger.info('Starting Server: (%s, %s)' % (ip, port))
    init_server(ip, port)
