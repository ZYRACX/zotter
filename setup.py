from setuptools import setup, find_packages

setup(
    name='dot jotter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'typer[all]',
        'rich',
    ],
    entry_points='''
        [console_scripts]
        notes=mynotes_cli.main:app
    ''',
)