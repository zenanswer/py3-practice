#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    tests.test_multiprocessing
    ~~~~~~~~~~~~~~~~~~~
    Some deom for the python
    `Process-based parallelism https://docs.python.org/3.7/library/multiprocessing.html#multiprocessing.pool.Pool`_
"""


import unittest
import time
from functools import wraps
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


def show_case_name(function):
    @wraps(function)
    def function_show_name(*args, **kwargs):
        print('=== %s ===' % function.__name__)
        return function(*args, **kwargs)
    return function_show_name


def calculate_cost(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        function(*args, **kwargs)
        t1 = time.time()
        print(
            "Total time running %s: %s seconds."
            % (function.__name__, str(t1-t0)))
        return t1-t0
    return function_timer


@calculate_cost
def hot_cpu(n):
    [i*i for i in range(n)]


def run_pool_test(pool):
    results = pool.map(
        hot_cpu,
        [50000000, 50000000, 50000000, 50000000])
    avg_time = sum(results)/len(results)
    print(
        "Avg time running : %s seconds."
        % (avg_time))


class TestSet(unittest.TestCase):

    @show_case_name
    def test_main_thread(self):
        hot_cpu(50000)

    @show_case_name
    def test_threadPool(self):
        pool = ThreadPool(4)
        run_pool_test(pool)

    @show_case_name
    def test_processingPool(self):
        pool = Pool(4)
        run_pool_test(pool)


if __name__ == '__main__':
    unittest.main()
