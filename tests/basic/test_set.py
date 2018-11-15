#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    tests.basic.test_set
    ~~~~~~~~~~~~~~~~~~~
    Some deom for the python set collection
    `Built-in Types - Set https://docs.python.org/3.5/library/stdtypes.html?highlight=set#set`_
"""


import unittest


class TestSet(unittest.TestCase):

    def test_construction(self):
        my_set = set([5, 2, 3, 3, 4, 1])
        print('my_set [%s]' % my_set)
        my_set_2 = {5, 2, 3, 3, 4, 1}
        self.assertAlmostEqual(my_set, my_set_2)

    def test_diff_with_list(self):
        my_list = [5, 2, 3, 3, 4, 1]
        my_set = set(my_list)
        self.assertNotEqual(len(my_list), len(my_set))

    def test_mathematical(self):
        my_set_1 = set([1, 3, 5, 7])
        my_set_2 = set([2, 4, 6, 7])
        # union
        self.assertEqual(my_set_1 | my_set_2, set([1, 2, 3, 4, 5, 6, 7]))
        # intersection
        self.assertEqual(my_set_1 & my_set_2, set([7]))
        # difference, elements in the set that are not in the others.
        self.assertEqual(my_set_1 - my_set_2, set([1, 3, 5]))
        # other, elements in either the set or other but not both.
        self.assertEqual(my_set_1 ^ my_set_2, set([1, 2, 3, 4, 5, 6]))

    def test_index(self):
        with self.assertRaises(TypeError):
            # TypeError: 'set' object does not support indexing
            my_set = set([1, 3, 5, 7])
            my_set[1]

    def test_slice(self):
        with self.assertRaises(TypeError):
            # TypeError: 'set' object is not subscriptable
            my_set = set([1, 3, 5, 7])
            my_set[1:2]

    def test_frozenset(self):
        with self.assertRaises(AttributeError):
            # AttributeError: 'frozenset' object has no attribute 'add'
            my_set = frozenset([1, 3, 5, 7])
            my_set.add(9)
        my_set = set([1, 3, 5, 7])
        my_set.add(9)
        self.assertEqual(len(my_set), 5)


if __name__ == '__main__':
    unittest.main()
