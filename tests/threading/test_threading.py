#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    tests.test_threading
    ~~~~~~~~~~~~~~~~~~~
    Some deom for the pythonhttps://docs.python.org/3/library/threading.html`_
"""


import unittest
import threading
import time
import random


class TestSet(unittest.TestCase):

    def test_counting(self):
        print('>>> test_counting')
        x = 0

        def do_count():
            nonlocal x
            print('[%s] do_count before x=[%d]'
                  % (threading.current_thread().name, x))
            x += 1
            print('[%s] do_count after x=[%d]'
                  % (threading.current_thread().name, x))
    
        thread_list = [
            threading.Thread(target=do_count, name=str(id)) for id in range(0, 20)]
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        print('X is [%d]' % x)

    def test_lock(self):
        print('>>> test_lock')
        q1 = []
        q2 = []
        lock = threading.RLock()

        def do_put():
            time.sleep(random.uniform(0, 1))
            nonlocal q1, q2, lock
            with lock:
                print(
                    '[%s] do_put before x=[%d,%d]'
                    % (threading.current_thread().name, len(q1), len(q2)))
                q1.append(threading.current_thread().name)
                time.sleep(random.uniform(0, 1))
                q2.append(threading.current_thread().name)
                print(
                    '[%s] do_put after x=[%d,%d]'
                    % (threading.current_thread().name, len(q1), len(q2)))

        thread_list = [
            threading.Thread(target=do_put, name=str(id))
            for id in range(0, 50)]
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        print('Q size is \n[%s]\n[%s]' % (q1, q2))

    def test_consumer_producer(self):
        print('>>> test_consumer_producer')
        q = []
        lock = threading.RLock()
        cond = threading.Condition(lock)

        def consumer(q, lock, cond):
            with cond:
                print('consumer [%s]'
                      % (threading.current_thread().name))
                # if len(q) == 0:
                while len(q) == 0:
                    cond.wait()
                print('consumer [%s] delete'
                      % (threading.current_thread().name))
                del q[0]

        def producer(q, lock, cond):
            with cond:
                print('producer [%s]'
                      % (threading.current_thread().name))
                q.append(threading.current_thread().name)
                cond.notify()

        thread_list = [
            (threading.Thread(
                target=consumer, name=str(id) + 'consumer',
                args=[q, lock, cond]),
             threading.Thread(
                 target=producer, name=str(id) + 'producer',
                 args=[q, lock, cond]))
            for id in range(0, 2)]
        for thread in thread_list:
            thread[0].start()
            thread[1].start()
        for thread in thread_list:
            thread[0].join()
            thread[1].join()
        print('Q size is [%s]' % q)

    def test_semaphore(self):
        print('>>> test_semaphore')
        sem = threading.BoundedSemaphore(5)
        x = 0

        def do_count():
            nonlocal x, sem
            with sem:
                print(
                    '[%s] do_count before x=[%d]'
                    % (threading.current_thread().name, x))
                time.sleep(random.uniform(0, 1))
                x += 1
                print(
                    '[%s] do_count after x=[%d]'
                    % (threading.current_thread().name, x))
    
        thread_list = [
            threading.Thread(target=do_count, name=str(id)) for id in range(0, 20)]
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        print('X is [%d]' % x)

if __name__ == '__main__':
    unittest.main()
