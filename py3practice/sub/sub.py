#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.sub.sub
    ~~~~~~~~~~~~~~~~~~~
    Here is dummy file for testing importing sub module.
    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""

from py3practice.util import comm


def sub_func():
    comm.comm()
    print('I\'m sub')
    return 0


if __name__ == '__main__':
    sub_func()
