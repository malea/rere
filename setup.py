"""
rere: regex redone
------------------

    from rere import *

    money_regex = Exactly('$') + Digit*2 + (Exactly('.') + Digit*2).zero_or_one

    regex.match('$23.95') # ==> True

Isn't this better than `regex.compile('\\\\$\\\\d\\\\d(\\\\.\\\\d\\\\d)?')`?

"""

from setuptools import setup

setup(
    name='rere',
    version='0.1.0',
    url='https://github.com/malea/rere',
    license='Apache 2',
    author='Malea Grubb',
    author_email='maleangrubb@gmail.com',
    description='regex redone',
    long_description=__doc__,
    py_modules=['rere'],
)
