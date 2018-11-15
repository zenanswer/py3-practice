#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    tests.basic.test_gen
    ~~~~~~~~~~~~~~~~~~~
    Some deom for the python `Generators https://python-course.eu/python3_generators.php`_
"""


import unittest
from collections.abc import Iterator


class TestSet(unittest.TestCase):

    def test_basic(self):
        def city_generator():
            yield("London")
            yield("Hamburg")
            yield("Konstanz")
            yield("Amsterdam")
            yield("Berlin")
            yield("Zurich")
            yield("Schaffhausen")
            yield("Stuttgart")

        cities = city_generator()
        for city in cities:
            print(city)

    def test_fibonacci(self):
        # fibonacci, Fn = Fn - 1 + Fn - 2 , F0 = 0 and F1 = 1
        def get_fibonacci_list(max):
            values = [0, 1]
            next = values[-1] + values[-2]
            while next < max:
                values.append(next)
                next = values[-1] + values[-2]
            return values
        self.assertIsInstance(get_fibonacci_list(14), list)
        self.assertEqual(get_fibonacci_list(14), [0, 1, 1, 2, 3, 5, 8, 13])

        def fibonacci_generator(max):
            prev = 0
            curr = 1
            while prev < max:
                yield prev
                prev, curr = curr, prev + curr
        self.assertIsInstance(fibonacci_generator(14), Iterator)
        self.assertEqual(list(fibonacci_generator(14)),
                         [0, 1, 1, 2, 3, 5, 8, 13])
        a_generator = fibonacci_generator(14)
        self.assertEqual(next(a_generator), 0)
        self.assertEqual(next(a_generator), 1)
        self.assertEqual(next(a_generator), 1)
        self.assertEqual(next(a_generator), 2)

    def test_return(self):
        def fibonacci_generator(max):
            prev = 0
            curr = 1
            while prev < max:
                yield prev
                if prev > 3:
                    # raise StopIteration('Force stop')
                    return 'Force stop'
                prev, curr = curr, prev + curr
        self.assertEqual(list(fibonacci_generator(14)),
                         [0, 1, 1, 2, 3, 5])

    def test_send(self):
        def double(max):
            value = 0
            while value < max:
                value = yield value
                value *= 2
        a_generator = double(20)
        self.assertEqual(next(a_generator), 0)
        self.assertEqual(a_generator.send(1), 2)
        self.assertEqual(a_generator.send(5), 10)
        with self.assertRaises(StopIteration):
            a_generator.send(10)

    def test_from(self):
        def from_two_range():
            yield range(0, 3)
            yield range(10, 12)
        for item in from_two_range():
            self.assertIsInstance(item, range)
        self.assertEqual(list(from_two_range()), [range(0, 3), range(10, 12)])

        def from_one_range():
            yield from range(0, 3)
            yield from range(10, 12)

        self.assertEqual(list(from_one_range()), [0, 1, 2, 10, 11])

    def test_sub_gen(self):
        def sub_gen():
            next = yield 0
            next = yield next
            return "Stop"

        def gen():
            yield from sub_gen()
            yield from sub_gen()

        a_generator = gen()
        self.assertEqual(next(a_generator), 0)
        self.assertEqual(a_generator.send(1), 1)
        self.assertEqual(a_generator.send(5), 0)
        self.assertEqual(a_generator.send(10), 10)
        with self.assertRaises(StopIteration):
            self.assertEqual(a_generator.send(50), 50)

    # TODO
    # Recursive Generators
    # A Generator of Generators


if __name__ == '__main__':
    unittest.main()
