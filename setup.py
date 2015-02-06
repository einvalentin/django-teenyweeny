import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'Readme.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-teenyweeny',
    version='1.1',
    packages=['teeny_weeny'],
    include_package_data=True,
    license='Apache License',  # example license
    description='A simple django app for manual url shortening.',
    long_description=README,
    url='https://github.com/einvalentin/django-teenyweeny',
    author='Valentin v. Seggern',
    author_email='valentin@crowflying.com',
)
