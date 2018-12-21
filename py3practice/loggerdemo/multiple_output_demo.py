#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.loggerdemo.multiple_output_demo
    ~~~~~~~~~~~~~~~~~~~
    A dummy main for demo the logging in multiple handlers and formatters

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""


import logging

f_formatter = logging.Formatter('FILE %(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('spam.log')
fh.setLevel(logging.ERROR)
fh.setFormatter(f_formatter)

c_formatter = logging.Formatter('CONSOLE %(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
ch.setFormatter(c_formatter)

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
