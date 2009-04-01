#!/usr/bin/env python
from distutils.core import setup

long_description = """python-xmltv is a Python module for reading XMLTV files.

More information on XMLTV can be found at http://membled.com/work/apps/xmltv/
"""

setup(name             = "python-xmltv",
      version	       = "1.3",
      description      = "A Python module for reading XMLTV files",
      long_description = long_description,
      author           = "James Oakley",
      author_email     = "jfunk@funktronics.ca",
      url              = "http://www.funktronics.ca/python-xmltv",
      license	       = "LGPL",
      py_modules       = ['xmltv'],
     )
