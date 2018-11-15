#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    tests.basic.test_list_com
    ~~~~~~~~~~~~~~~~~~~
    Some deom for the python `List Comprehension https://python-course.eu/python3_list_comprehension.php`_
"""


import unittest


class TestSet(unittest.TestCase):

    def test_basic(self):
        Celsius = [39.2, 36.5, 37.3, 37.8]
        Fahrenheit = [
            102.56, 97.700000000000003,
            99.140000000000001,
            100.03999999999999]

        def get_fahrenheit(celsius):
            for cel in celsius:
                yield ((float(9)/5)*cel + 32)
        self.assertEqual(list(get_fahrenheit(Celsius)), Fahrenheit)

        fahrenheit = [((float(9)/5)*x + 32) for x in Celsius]
        self.assertEqual(fahrenheit, Fahrenheit)

    def test_if(self):
        def get_results_with_list():
            results = []
            for x in range(1, 30):
                for y in range(x, 30):
                    for z in range(y, 30):
                        if x**2 + y**2 == z**2:
                            results.append((x, y, z))
            return results

        def get_results_with_gen():
            for x in range(1, 30):
                for y in range(x, 30):
                    for z in range(y, 30):
                        if x**2 + y**2 == z**2:
                            yield (x, y, z)
        results = [
            (x, y, z)
            for x in range(1, 30)
            for y in range(x, 30)
            for z in range(y, 30)
            if x**2 + y**2 == z**2]

        self.assertEqual(get_results_with_list(), results)
        self.assertEqual(list(get_results_with_gen()), results)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)
        self.assertEqual(results[0], (3, 4, 5))
        self.assertEqual(results[3], (7, 24, 25))

        results = [
            (x, y, z)
            for x in range(1, 30)
            for y in range(x, 30)
            for z in range(y, 30)
            if x**2 + y**2 == z**2
            if x < 10]
        self.assertEqual(len(results), 6)


if __name__ == '__main__':
    unittest.main()
