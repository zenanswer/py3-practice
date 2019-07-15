#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.caseLog2xls
    ~~~~~~~~~~~~~~~~~~~
    Load case_log file and converting data into a xls file.

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""

import traceback
import re
import datetime
import sqlite3
import os

import py3practice.csv2xls as py3csv


def get_record(file_path):
    """Getting the raw date from the input log file by line.

    :param file_path: the file path of the input case log file.
    :return: a generator, an :class:`generator` object.
    """
    with open(file_path, 'r', encoding='utf8') as log_file:
        for line in log_file:
            yield line


def formated_line(raw_line_generator):
    """Converting a raw line into a formated struct with regular expression

    :param raw_line_generator: return every raw line in file.
    :return: a generator, an :class:`generator` object.
    """
    for line in raw_line_generator:
        # print('RAW_LINE[%s]' % repr(line))
        # http://www.runoob.com/python/python-reg-expressions.html
        res = re.search(r'(?P<time>\d{2}/\d{2} \d{2}:\d{2}:\d{2},\d{3}) : (?P<type>\S*) (?P<name>\S*) \[(?P<state>\S*)\].*', line)
        if res is None or res.groupdict()['name'] is '':
            continue
        if res.groupdict()['type'] not in ['OPERATION', 'ACTION', 'PYTHONFUNC']:
            continue
        infos = res.groupdict()
        yield (infos['time'], infos['type'], infos['name'], infos['state'])


def get_duration(formated_line_generator):
    """Calculating the duration for every action and operation

    :param formated_line_generator: return formated line
    :return: a generator, an :class:`generator` object.
    """
    line_stack = []
    for (op_time, op_type, op_name, state) in formated_line_generator:
        # print(repr(line))
        if state == 'started':
            line_stack.append((op_time, op_type, op_name, state))
            continue
        if state == 'finished':
            if op_name == line_stack[-1][2]:
                last_line = line_stack.pop()
                # https://docs.python.org/3.5/library/datetime.html
                start_time = datetime.datetime.strptime(
                    last_line[0] + '000', r'%m/%d %H:%M:%S,%f')
                end_time = datetime.datetime.strptime(
                    op_time + '000', r'%m/%d %H:%M:%S,%f')
                duration = end_time - start_time
                yield (last_line[0], op_time, op_type, op_name,
                       duration.total_seconds())
            else:
                # TODO should stop all, because some log is missing.
                pass


def list_durations(duration_generator):
    """Saving the info into a sqllite DB and list the durations

    :param duration_generator: return duration for action and operation
    :return: a generator, an :class:`generator` object.
    """
    if os.path.isfile('example.db'):
        os.remove('example.db')
    # https://docs.python.org/3.5/library/sqlite3.html
    with sqlite3.connect('example.db') as conn:
        c = conn.cursor()
        # Create table
        c.execute(
            'CREATE TABLE duration_temps '
            '(start_time text, type text, name text, duration real)')
        for (start_time, _, op_type, op_name, duration) in duration_generator:
            c.execute(
                "INSERT INTO duration_temps "
                "(start_time, type, name, duration) "
                "VALUES ('%s', '%s', '%s', %f)" %
                (start_time, op_type, op_name, duration))
        conn.commit()

        for row in c.execute(
            """
            SELECT type, name, AVG(duration) AS 'avg_duration',
                count(name) AS 'count'
            FROM duration_temps
            GROUP BY type, name
            ORDER by type, avg_duration
            """
        ):
            # TODO wirte into a xls file
            print(row)


def process(input, output):

    raw_line_generator = get_record(input)
    formated_line_generator = formated_line(raw_line_generator)
    duration_generator = get_duration(formated_line_generator)
    list_durations(duration_generator)


if __name__ == '__main__':
    try:
        arg = py3csv.process_argv()
        process(arg.inputcsv, arg.outputxls)
    except Exception as exp:
        print(exp)
        traceback.print_exc()
