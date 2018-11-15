#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
from distutils.command.clean import clean
from sphinx.setup_command import BuildDoc
import unittest

"""
Release package tool for py3practice
"""

__copyright__ = "Copyright 2018, zenanswer"


name = "py3practice"
version = "1.0.0"
release = "dummy"


class CleanCommand(clean):

    description = 'Custom clean command to tidy up the project root.'
    user_options = []

    CLEAN_FILES = [
        'build',
        'dist',
        '*.egg-info',
        'docs/_build'
        ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import glob
        import os
        import shutil

        for path_spec in self.CLEAN_FILES:
            abs_paths = glob.glob(path_spec)
            for path in [str(p) for p in abs_paths]:
                print('removing %s' % os.path.relpath(path))
                shutil.rmtree(path)


def get_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(
    name=name,
    version=version,
    keywords=["python3", "practice"],
    description="practice for python3",
    long_description="This is demo REPO. for internal training.",
    license="MIT Licence",

    url="https://github.com/zenanswer/py3-practice",
    author="zenanswer",

    # packages=['py3practice', 'py3practice.sub', 'py3practice.util'],
    packages=find_packages(exclude=['tests', 'tests.*', 'docs']),

    include_package_data=True,
    exclude_package_data={'': ['.gitignore']},

    platforms="any",
    install_requires=[
        'xlwt>=1.3.0'
    ],
    dependency_links=[
    ],
    cmdclass={
        'clean': CleanCommand,
        'build_sphinx': BuildDoc
    },
    test_suite='setup.get_test_suite',

    # scripts=[],
    # entry_points={
    #     'console_scripts': [
    #         'test=test.help:main'
    #     ]
    # }
)
