#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read_from_root(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()

# CLASSIFIERS = [
#     'Development Status :: 4 - Beta',
#     'Environment :: Web Environment',
#     'Framework :: Django',
#     'Intended Audience :: Developers',
#     'License :: OSI Approved :: BSD License',
#     'Operating System :: OS Independent',
#     'Programming Language :: Python',
#     'Topic :: Internet :: WWW/HTTP',
# ]


setup(
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    name='python-version-info',
    # version='.'.join(str(v) for v in templatefinder.VERSION),
    description='python-version-info',
    long_description=read_from_root('README.rst'),
    url='https://github.com/TyMaszWeb/python-version-info',
    license='MIT License',
    platforms=['OS Independent'],
    # classifiers=CLASSIFIERS,
    install_requires=read_from_root('requirements.txt').split(),
    tests_require=read_from_root('test-requirements.txt').split(),
    packages=find_packages(),
    # include_package_data=False,
    # test_suite='runtests.main',
)
