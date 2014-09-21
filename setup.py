#/usr/bin/env python
import io
from setuptools import setup


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name='rubicon',
    version='0.0.0',
    description='A collection of tools to bridge between Python and other language environments.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/rubicon',
    packages=[],
    license='New BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets',
    ],
)
