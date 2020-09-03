#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://www.runoob.com/python/python-tutorial.html

"""
    py3practice.basics
    ~~~~~~~~~~~~~~~~~~~
    Basic for python.

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""


import sys


def get_interpreter_version():
    """ Get the version of this running interpreter
    :return: a :class:`string`
    """
    return sys.version_info


def get_platform():
    """Get the type of the platform

    :return: a :class:`string` object as below.

    +----------------+----------------+
    | System         | platform value |
    +================+================+
    | Linux          | 'linux'        |
    +----------------+----------------+
    | Windows        | 'win32'        |
    +----------------+----------------+
    | Windows/Cygwin | 'cygwin'       |
    +----------------+----------------+
    | Mac OS X       | 'darwin'       |
    +----------------+----------------+
    """
    # import platform
    # platform.platform()
    return sys.platform


if __name__ == '__main__':
    print("Interpreter Version: {}".format(get_interpreter_version()))
    print(f"Platform: {get_platform()}")
