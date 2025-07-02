# programa_CRM_/setup.py

from setuptools import setup, find_packages

setup(
    name='programa_CRM',
    version='1.0.0',
    description='Sistema CRM por consola en Python',
    author='Maria Jose Suarez',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python>=8.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
