#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    tests.basic.test_dict
    ~~~~~~~~~~~~~~~~~~~
    Some deom for the python dict collection
    `Built-in Types - Set https://docs.python.org/3.5/library/stdtypes.html?#dict`_
"""


import unittest


class TestSet(unittest.TestCase):

    def test_construction(self):
        a = dict(one=1, two=2, three=3)
        b = {'one': 1, 'two': 2, 'three': 3}
        c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
        d = dict([('two', 2), ('one', 1), ('three', 3)])
        e = dict({'three': 3, 'one': 1, 'two': 2})
        for a_dict in [b, c, d, e]:
            self.assertEqual(a, a_dict)

    def test_iter(self):
        my_dict = {'one': 1, 'two': 2, 'three': 3}
        self.assertEqual(list(my_dict.keys()), ['one', 'two', 'three'])
        self.assertEqual(list(my_dict.values()), [1, 2, 3])

        values = []
        for key in my_dict:
            values.append(my_dict[key])
        self.assertEqual(list(my_dict.values()), values)

        other_dict = {}
        for key, value in my_dict.items():
            other_dict[key] = value
        self.assertEqual(my_dict, other_dict)


if __name__ == '__main__':
    unittest.main()
