#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.loggerdemo.auxiliary
    ~~~~~~~~~~~~~~~~~~~
    A dummy module for demo the logging

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""


import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')


def some_function():
    module_logger.info('received a call to "some_function"')
