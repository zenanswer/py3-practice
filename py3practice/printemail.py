#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.printemail
    ~~~~~~~~~~~~~~~~~~~
    Parser a email file.

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""


import sys
import os
import traceback
import argparse
from email.parser import BytesParser

import py3practice.printLastMail as py3lm


def process_argv():
    """Processing input arguments

    :return: input args, has to be an instance of :attr:`argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__))
    parser.add_argument('--file', '-f',
                        help='The file path of the mail.',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    try:
        arg = process_argv()
        if not os.path.isfile(arg.file):
            print('No file found:', arg.file)
            sys.exit(1)
        with open(arg.file, 'rb') as mail:
            message = BytesParser().parsebytes(mail.read())
            py3lm.process_email(message)

    except Exception as exp:
        print(exp)
        traceback.print_exc()
