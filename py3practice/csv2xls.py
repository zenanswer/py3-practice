#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.csv2xls
    ~~~~~~~~~~~~~~~~~~~
    Load csv file and converting data into a xls file.

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""


import argparse
import traceback
import csv
import xlwt


def load_csv(file_name):
    """Loading a csv file as a specific format

    :param file_name: the path of the input csv file.
    :return: a new content list or the csv file,
             has to be an instance of :class:`list`.
    """
    with open(file_name, 'r', encoding='utf8') as csv_file:
        # iterator, list(iterator)
        lines = list(csv.reader(csv_file, delimiter='，'))
        # list comprehension
        lines = [line for line in lines if len(line) > 0]
        # list slice
        lines_sorted = lines[0:1] + sorted(lines[1:len(lines)])
        print('The sorted content:')
        print(lines_sorted)
    return lines_sorted


def get_style(forecolor, bold):
    """Generate a style for specified forecolor and has bold or not

    :param forecolor: the name of the forecolor.
    :param bold: has bold or not.
    :return: a style, an :class:`XFstyle` object.
    """
    # https://secure.simplistix.co.uk/svn/xlwt/trunk/xlwt/Style.py
    # https://www.crifan.com/python_xlwt_set_cell_background_color/
    style = xlwt.easyxf(
        'pattern: pattern solid, fore_colour %s; font: bold %s;' % (
            forecolor, bold))
    return style


def export_xls(content, file_name):
    """Exporting the content into sa xls file as a specific format

    :param content: the content loaded from csv file.
    :param file_name: the path of the output xls file.
    """
    excel_file = xlwt.Workbook(encoding='ascii')
    new_sheet = excel_file.add_sheet('库存状态', cell_overwrite_ok='True')
    for row_num, row in enumerate(content):
        style = xlwt.Style.default_style
        if row_num == 0:
            style = get_style('aqua', 'on')
        elif row[2] == '无货':
            style = get_style('yellow', 'off')
        elif len(row) < 4 or row[3] == '':
            style = get_style('red', 'off')
        for col_num, column in enumerate(row):
            new_sheet.write(row_num, col_num, column, style)
    print(new_sheet.get_height())
    print(new_sheet.get())
    excel_file.save(file_name)


def process_argv():
    """Processing input arguments

    :return: input args, has to be an instance of :attr:`argparse.Namespace`.
    """
    parser = argparse.ArgumentParser(prog='csv2xls')
    parser.add_argument('--inputcsv', '-i',
                        help='The file path of input csv file.',
                        required=True)
    parser.add_argument('--outputxls', '-o',
                        help='The file path of output xls file.',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    try:
        arg = process_argv()
        content = load_csv(arg.inputcsv)
        export_xls(content, arg.outputxls)
    except Exception as exp:
        print(exp)
        traceback.print_exc()
