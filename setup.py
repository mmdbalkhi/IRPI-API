#!/usr/bin/env python3
import sys

from setuptools import setup  # type: ignore

if sys.version_info < (3, 7, 0):
    sys.exit("Python 3.7 or later is required. ")

setup(install_requires=["flask"])
