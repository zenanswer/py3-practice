#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    tests.basic.test_iter
    ~~~~~~~~~~~~~~~~~~~
    Some deom for the python `Iterators and Iterables https://python-course.eu/python3_iterable_iterator.php`_
    You can iterate with a for loop over iterators and iterables.
    Every iterator is also an iterable, but not every iterable is an iterator.

    http://kuanghy.github.io/2016/05/18/python-iteration
"""


import unittest


class TestSet(unittest.TestCase):

    def test_iterable(self):
        print('==== test_iterable ====')

        class MyIterable:
            def __init__(self):
                print('MyIterable __init__')
                self.list = [1, 2, 3, 4]

            def __getitem__(self, i):
                print('MyIterable __getitem__ index:' + str(i))
                if i >= len(self.list) or i < 0:
                    raise IndexError('IndexError in IterableGetItem')
                return self.list[i]

        def loop_iterable(iterable):
            print('==== test_iterable loop_iterable ====')
            values = []
            for item in iterable:
                values.append(item)
            self.assertEqual(values, iterable.list)

        my_iterable = MyIterable()
        loop_iterable(my_iterable)
        loop_iterable(my_iterable)

    def test_iterator(self):
        print('==== test_iterator ====')

        class MyIterator:
            def __init__(self):
                print('MyIterator __init__')
                self.list = [1, 2, 3, 4]
                self.index = 0
            
            def __iter__(self):
                print('MyIterator __iter__')
                return self

            def __next__(self):
                print('MyIterator __next__ [%d]' % self.index)
                self.index += 1
                if self.index > len(self.list):
                    # self.index = 0
                    raise StopIteration('StopIteration index=%s' % self.index)
                return self.list[self.index-1]

        def loop_iterator(iterator):
            print('==== test_iterator loop_iterator ====')
            values = []
            for item in iterator:
                values.append(item)
            self.assertEqual(values, iterator.list)

        my_iterator = MyIterator()
        loop_iterator(my_iterator)
        loop_iterator(my_iterator)

    def test_iterator_and_iterable(self):
        print('==== test_iterator_and_iterable ====')

        class MyIterator:
            def __init__(self):
                print('MyIterator __init__')
                self.list = [1, 2, 3, 4]
                self.index = 0

            def __next__(self):
                print('MyIterator __next__ [%d]' % self.index)
                self.index += 1
                if self.index > len(self.list):
                    raise StopIteration('StopIteration index=%s' % self.index)
                return self.list[self.index-1]

        class MyIterable:
            def __init__(self):
                print('MyIterable __init__')
                self.my_iterator = MyIterator()

            def __iter__(self):
                print('MyIterable __iter__')
                return self.my_iterator

        my_iterable = MyIterable()
        values = []
        for item in my_iterable:
            values.append(item)
        self.assertEqual(values, my_iterable.my_iterator.list)

        """
            Iterable: __getitem__(self, i) or __iter__(self)
            Iterator: __next__(self)
        """

    def test_iterator_and_iterable_v2(self):
        print('==== test_iterator_and_iterable_v2 ====')

        class MyIterator_1:
            def __init__(self, a_list):
                print('MyIterator_1 __init__')
                self.list = a_list
                self.index = 0

            def __next__(self):
                print('MyIterator_1 __next__ [%d]' % self.index)
                self.index += 1
                if self.index > len(self.list):
                    raise StopIteration('StopIteration index=%s' % self.index)
                return self.list[self.index-1]

        class MyIterator_2:
            def __init__(self, an_iterator):
                print('MyIterator_2 __init__')
                self.an_iterator = an_iterator
                self.index = 0

            def __next__(self):
                print('MyIterator_2 __next__ [%d]' % self.index)
                self.index += 2
                try:
                    return self.an_iterator[self.index-1]
                except IndexError:
                    raise StopIteration('StopIteration index=%s' % self.index)

        class MyIterable:
            def __init__(self, step_type=1):
                print('MyIterable __init__')
                self.step_type = step_type
                self.list = [1, 2, 3, 4]

            def set_step_type(self, step_type):
                self.step_type = step_type

            def __iter__(self):
                print('MyIterable __iter__')
                if self.step_type == 1:
                    return MyIterator_1(self.list)
                return MyIterator_2(self)

            def __getitem__(self, i):
                print('MyIterable __getitem__ index:' + str(i))
                if i >= len(self.list) or i < 0:
                    raise IndexError('IndexError in IterableGetItem')
                return self.list[i]

        my_iterable = MyIterable()
        values = []
        for item in my_iterable:
            values.append(item)
        self.assertEqual(values, [1, 2, 3, 4])

        my_iterable = MyIterable()
        my_iterable.set_step_type(2)
        values = []
        for item in my_iterable:
            values.append(item)
        self.assertEqual(values, [2, 4])


if __name__ == '__main__':
    unittest.main()
