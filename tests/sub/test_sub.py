#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

import py3practice.sub.sub as sub


class TestSubModule(unittest.TestCase):

    def test_sub_func(self):
        ret = sub.sub_func()
        self.assertEqual(ret, 0)


if __name__ == '__main__':
    unittest.main()
