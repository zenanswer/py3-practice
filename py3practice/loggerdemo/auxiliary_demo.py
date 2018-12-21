#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.loggerdemo.auxiliary_demo
    ~~~~~~~~~~~~~~~~~~~
    A dummy main for demo the logging

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""


import logging
import auxiliary


# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':
    logger.info('creating an instance of auxiliary_module.Auxiliary')
    a = auxiliary.Auxiliary()
    logger.info('created an instance of auxiliary_module.Auxiliary')
    logger.info('calling auxiliary_module.Auxiliary.do_something')
    a.do_something()
    logger.info('finished auxiliary_module.Auxiliary.do_something')
    logger.info('calling auxiliary_module.some_function()')
    auxiliary.some_function()
    logger.info('done with auxiliary_module.some_function()')
