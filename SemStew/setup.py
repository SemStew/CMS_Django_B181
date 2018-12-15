import os
import re
import sys

if sys.version_info[:3] < (3, 7):
    sys.exit("virtualenv requires Python 3.7 or higher.")
try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

        def initialize_options(self):
            TestCommand.initialize_options(self)
            self.pytest_args = []

        def finalize_options(self):
            TestCommand.finalize_options(self)
            # self.test_args = []
            # self.test_suite = True

        def run_tests(self):
            # import here, because outside the eggs aren't loaded
            import pytest

            sys.exit(pytest.main(self.pytest_args))

    setup_params = {
        "entry_points": {"console_scripts": ["virtualenv=virtualenv:main"]},
        "zip_safe": False,
        "cmdclass": {"test": PyTest},
        "tests_require": ["pytest", "mock"],
    }
except ImportError:
    from distutils.core import setup

    if sys.platform == "win32":
        print("Note: without Setuptools installed you will " 'have to use "python -m virtualenv ENV"')
        setup_params = {}
    else:
        script = "src/scripts/virtualenv"
        setup_params = {"scripts": [script]}


def read_file(*paths):
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, *paths)) as f:
        return f.read()


# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing  # noqa
except ImportError:
    pass

with open(os.path.join(os.path.dirname(__file__), '../README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='SemStew',
    version='1.0',
    packages=find_packages(),
    description='Template for restaurant web pages',
    license='MIT',
    url='https://github.com/SemStew/CMS_Django_B181',
    scripts=['manage.py'],
    install_requires=[
        'Django>=2.1.4',
        'djangorestframework>=3.9.0'
    ],
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