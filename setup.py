"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Africa\'sTalking SMS Dashboard,
    version='0.0.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mosesokemwa/sms_dashboard',
    author='Todd Birchard',
    author_email='okemwamoses@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Flask Flask-Assets Blueprints Africa\'sTalking',
    packages=find_packages(),
    install_requires=['Flask',
                      'Flask_assets',
                      'Africa\'sTalking'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'install=wsgi:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/mosesokemwa/sms_dahsboard/issues',
        'Source': 'https://github.com/mosesokemwa/sms_dahsboard/',
    },
)
