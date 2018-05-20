#!/usr/bin/env python

from setuptools import setup

def read_description():
    import os
    path = os.path.join(os.path.dirname(__file__), 'README.rst')
    try:
        with open(path) as f:
            return f.read()
    except:
        return 'No description found'

setup(
    name='deluge-client',
    version='1.5.0',
    description='Simple Deluge Client',
    long_description=read_description(),
    author='Anders Jensen',
    author_email='johndoee+delugeclient@tidalstream.org',
    maintainer='John Doee',
    url='https://github.com/JohnDoee/deluge-client',
    packages=['deluge_client'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
