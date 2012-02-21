#!/usr/bin/env python
from distutils.core import setup

setup(
    name="python-xmltv",
    description="A Python Module for Reading and Writing XMLTV Files",
    version="1.4",
    author="James Oakley",
    author_email="jfunk@funktronics.ca",
    url= "http://bitbucket.org/jfunk/python-xmltv",
    py_modules=['xmltv'],
    long_description=open('README.txt').read() + '\n\n' +
                     open('CHANGELOG.txt').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license="LGPL-3.0+",
)
