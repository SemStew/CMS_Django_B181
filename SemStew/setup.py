import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), '../README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='SemStew',
    version='1.0',
    packages=find_packages(),
    description='Template for restaurant web pages',
    license='MIT licence',
    url='https://github.com/SemStew/CMS_Django_B181',
    scripts=['manage.py'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1.4',  
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)