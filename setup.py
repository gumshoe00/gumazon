#!/usr/bin/env python

"""The setup script."""

# TIMELINE.rst ---------------------------
# cat<<EOF > TIMELINE.rst
# =========
# TIMELINE
# =========
#
# EOF
# git log >> docs/TIMELINE.rst
#
# FEATURES.rst ---------------------------
# ----- CREATE
# cat<<EOF > FEATURES.rst
# ========
# Features
# ========
#
#
# EOF
# ----- UPDATE: Append new feature.__doc__
# git log >> docs/TIMELINE.rst

from setuptools import setup, find_packages

with open('docs/README.rst') as readme_file:
    readme = readme_file.read()


with open('docs/HISTORY.rst') as history_file:
    readme += '\n\n'+history_file.read()


with open('docs/TIMELINE.rst') as timeline_file:
    readme += '\n\n'+timeline_file.read()


requirements = [ ]

test_requirements = ['pytest>=3', ]

classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python :: >=2.7',
    'Programming Language :: Python :: =<3.9',
]

setup(
    name='gumazon',
    description="Gumazon Application",
    author="Gumshoe Media Inc.",
    author_email='admin@gumazon.io',
    version='0.1.1',
    python_requires='<=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'gumazon=gumazon.__main__:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords='gumazon',
    packages=find_packages(include=['gumazon', 'gumazon.*']),
    test_suite='tests',
    tests_require=['pytest>=3', ],
    url='https://github.com/gumshoe00/gumazon',
    zip_safe=False,
)
