##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.event package

$Id$
"""

import os
import sys
from setuptools import setup, find_packages
if sys.version_info < (3,):
    extra = {}
else:
    # Python 3 support:
    extra = dict(
      use_2to3=True,
      convert_2to3_doctests=['docs/index.rst'],
    )

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='zope.event',
    version='3.4.2dev',
    url='http://pypi.python.org/pypi/zope.event',
    license='ZPL 2.1',
    description='Very basic event publishing system',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description=(
        read('README.txt')
        + '\n' +
        read('CHANGES.txt')
        ),
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope',],
      include_package_data=True,
      install_requires=['setuptools'],
      zip_safe=False,
      test_suite='zope.event.tests.test_suite',
      **extra
      )
