import os
from setuptools import setup, find_packages
import md_playerpointer_users


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="md-playerpointer-users",
    version=md_playerpointer_users.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, metrics, dashboard, widget, playerpointer',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/md-playerpointer-users",
    packages=find_packages(),
    include_package_data=True,
)
