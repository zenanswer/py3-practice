#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.printLastMail
    ~~~~~~~~~~~~~~~~~~~
    Print the last email in the InBox.

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""

import os
import argparse
import traceback
import getpass
import poplib
from email.parser import BytesParser
from email.header import decode_header
from email.utils import parseaddr
import time


def retrieve_last_mail(address, port, tls, username, password):
    print('Try to connect to pop3 server.')
    pop3_handler = None
    if tls:
        pop3_handler = poplib.POP3_SSL(address, port=port)
    else:
        pop3_handler = poplib.POP3(address, port=port)
    print(pop3_handler.user(username))
    print(pop3_handler.pass_(password))
    resp, mails, _ = pop3_handler.list()
    print(resp)
    count = len(mails) - 1
    print('Mial count: %d' % count)
    resp, lines, _ = pop3_handler.retr(count)
    print(resp)
    msg_content = b'\r\n'.join(lines)
    message = BytesParser().parsebytes(msg_content)
    # msg_content = b'\r\n'.join(lines).decode('utf-8')
    # message = Parser().parsestr(msg_content)
    pop3_handler.quit()
    return message


def process_email(message):
    process_mail_header(message)
    process_mail_body(message)


def process_mail_header(message):
    def decode_str(raw_data):
        value, charset = decode_header(raw_data)[0]
        if charset:
            value = value.decode(charset)
        return value

    def parser_address(raw_data):
        hdr, addr = parseaddr(raw_data)
        name = decode_str(hdr)
        return (u'%s <%s>' % (name, addr))

    def parser_addresses(raw_data):
        address_list = raw_data.split(',')
        return [parser_address(item) for item in address_list]

    for header, parser_func in {
            'Subject': decode_str,
            'From': parser_address,
            'To': parser_addresses,
            'Cc': parser_addresses}.items():
        value = message.get(header, '')
        value = parser_func(value)
        print('%s: %s' % (header, value))


def process_mail_body(message):
    if (message.is_multipart()):
        parts = message.get_payload()
        for part in parts:
            process_mail_body(part)
    else:
        def guess_charset(msg):
            charset = msg.get_charset()
            if charset is None:
                content_type = msg.get('Content-Type', '').lower()
                pos = content_type.find('charset=')
                if pos >= 0:
                    charset = content_type[pos + 8:].strip()
            return charset

        def saveas_attachment(message):
            content_type = message.get_content_type()
            file_prefix, file_ext = content_type.split('/')
            file_path = os.path.join(
                os.getcwd(),
                file_prefix + '_' + time.strftime("%H_%M_%S") + '.' + file_ext)
            with open(file_path, 'wb') as image_file:
                image_file.write(message.get_payload(decode=True))
            print(
                f'Save [{message.get("Content-ID")}] '
                f'[{content_type}] '
                f'as [{file_path}].')

        def save_attachment(message):
            file_path = os.path.join(
                os.getcwd(),
                message.get_filename())
            with open(file_path, 'wb') as image_file:
                image_file.write(message.get_payload(decode=True))
            print(
                f'Save [{message.get("Content-ID")}] '
                f'[{message.get_filename()}] '
                f'as [{file_path}].')

        content_type = message.get_content_type()
        if content_type in ['text/plain']:
            content = message.get_payload(decode=True)
            charset = guess_charset(message)
            if charset:
                content = content.decode(charset)
            print('Content: %s' % content)
        elif content_type == 'text/html':
            saveas_attachment(message)
        elif content_type.split('/')[0] == 'image':
            save_attachment(message)
        else:
            print('Oter content type: %s' % content_type)


def process_argv():
    """Processing input arguments

    :return: input args, has to be an instance of :attr:`argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__))
    parser.add_argument('--pop3address', '-a',
                        help='The address of the pop3 server.',
                        required=True)
    parser.add_argument('--port', '-p',
                        type=int,
                        default=110,
                        help="The port number for pop3")
    parser.add_argument('--username', '-u',
                        help='The user name of this email account',
                        required=True)
    parser.add_argument('--no-tls', dest='tls',
                        action='store_false',
                        default=True,
                        help='Disable TLS/SSl')
    # parser.add_argument('--password', '-p',
    #                     help='The pass word of this email account',
    #                     required=True)
    # password = input('Password: ')
    password = getpass.getpass("Enter your password: ")
    return (parser.parse_args(), password)


if __name__ == '__main__':
    try:
        arg, password = process_argv()
        message = retrieve_last_mail(
            arg.pop3address,
            arg.port,
            arg.tls,
            arg.username,
            password)
        process_email(message)
    except Exception as exp:
        print(exp)
        traceback.print_exc()
