# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com
'''


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='somedata',
    version='0.1.1',
    packages=['somedata'],
    package_data={
         'somedata': ['source/*.json', 'source/*.txt', 'source/en/*.txt', 'source/ko/*.txt'],
    },
    author='Taehong Kim',
    author_email='peppy0510@hotmail.com',
    description='',
    long_description='',
)