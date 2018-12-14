import os
from setuptools import find_packages, setup

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	#setup for whole app to start properly
	python -m pip install --upgrade pip setuptools wheel
	python3 -m venv venv
	source venv/bin/activate
	pip install Django
	pip install djangorestframework
	python manage.py makemigrations
	python manage.py migrate

    name='semstew',
    version='1.0',
    description='Serves as a template for restaurant web pages',
    license='MIT licence',
    url='https://github.com/SemStew/CMS_Django_B181',
	scripts=['manage.py'],
	classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',  
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