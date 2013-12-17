# Filename: setup.py

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

with open('LICENSE') as fin:
    LICENSE = fin.read()

MODULES = ['gvmagic']

setup(
    name='ipython-magic',
    version='0.1',

    author="Chris Drake",
    author_email="cjdrake AT gmail DOT com",
    description="IPython magic functions",
    license=LICENSE,
    url="https://github.com/cjdrake/ipython-magic",

    py_modules=MODULES,
)

