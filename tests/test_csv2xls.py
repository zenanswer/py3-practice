#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

import py3practice.csv2xls as csv2xls


class TestCSV2XLS(unittest.TestCase):

    def test_load_csv(self):
        content = csv2xls.load_csv('other/库存状态.txt')
        self.assertEqual(len(content), 4)
        self.assertEqual(len(content[0]), 4)
        self.assertEqual(len(content[3]), 3)
        self.assertIn('USB', content[1])
        self.assertEqual('未知', content[3][2])


if __name__ == '__main__':
    unittest.main()
