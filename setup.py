from setuptools import setup, find_packages

setup(
    name='catastro-lib-python',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/sperea/catastro-lib-python',
    license='GPLv3',
    author='Sergio Perea',
    author_email='sperea@gmail.com',
    install_requires=[
        'requests',
        'xmltodict',
        'json',
    ],
    description='Module for Portal de la Dirección General del Catastro'
)