#!/usr/bin/env python
import numpy as np
import os

#import pkgconfig
from setuptools import setup, find_packages


# http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2


# setup(name='pywren',
#       version='1.0',
#       description='Simple python lambda client for embarassing parallelism',
#       author='Eric Jonas',
#       author_email='jonas@eecs.berkeley.edu',
#       url='https://www.github.com/ericmjonas/pywren/',
#       packages=['pywren'],
#       scripts=['bin/pywren']
#      )


setup(
    name='pywren',
    version='1.0',
    packages=['pywren', 'pywren.scripts'],
    install_requires=[
        'numpy', 'Click', 'boto3', 'cloudpickle', 'PyYAML', 'enum34' 
    ],
    entry_points = 
    { 'console_scripts' : ['pywren=pywren.scripts.pywrencli:cli']}, 
    include_package_data=True
)