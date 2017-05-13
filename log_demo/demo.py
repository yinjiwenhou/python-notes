#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()  
logger.setLevel(logging.DEBUG)

LOG_PATH = './logger.txt'
fh = RotatingFileHandler(LOG_PATH, maxBytes=10*1024*1024, backupCount=5)
fh.setLevel(logging.DEBUG)
fh_formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setFormatter(fh_formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch_formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
ch.setFormatter(ch_formatter)

logger.addHandler(fh)
logger.addHandler(ch)


logging.debug('hello')
logging.info('info')
