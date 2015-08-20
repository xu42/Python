try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'cet',
    version = '0.1.1',
    keywords = ('cet', 'CET', 'grades'),
    description = 'Access to College English Test Band 4 and Band 6 Grades',
    license = 'MIT License',

    author = 'xu42',
    author_email = 'x@xuyangjie.cn',
    url = 'https://xuyangjie.cn/',
    
    py_modules = ['cet']
)
