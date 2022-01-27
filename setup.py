from setuptools import setup, find_packages

readme = []
with open('README.rst') as readme_file:
    readme.extend(readme_file.readlines())

history = []
with open('HISTORY.rst') as history_file:
    history.extend(history_file.readlines())

requirements = []
with open('requirements.txt') as requirements_file:
    requirements.extend(requirements_file.readlines())


setup(
    name='gumazon',
    keywords='Gumazon Ads Cross-Locals Visibility.',
    url='https://github.com/gumshoe00/gumazon',
    version='0.1.0',
    author='Gumshoe Media Inc.',
    author_email='gumshoe.media.inc@gmail.com',
    python_requires='=<3.9.1',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: >=2.7',
        'Programming Language :: Python :: =<3.9.1',
    ],
    description="Gumazon Ads Cross-Locals Visibility.",
    entry_points={
        'console_scripts': [
            'gumazon=gumazon.__main__',
        ],
    },
    install_requires=requirements,
    license='GNU General Public License v3',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)

