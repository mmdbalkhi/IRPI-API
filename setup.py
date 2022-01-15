import sys

from setuptools import setup

if sys.version_info < (3, 6, 0):
    sys.exit(
        "Python 3.6 or later is required. "
        "See https://github.com/pypa/pipx "
        "for installation instructions."
    )

if __name__ == "__main__":
    setup()
