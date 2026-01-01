from setuptools import setup, find_packages

setup(
    name='zotter',              # <--- Updated Name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'typer[all]',
        'rich',
    ],
    entry_points='''
        [console_scripts]
        zotter=zotter.main:app 
    ''',
)