#! /usr/bin/env python
"""
Set up for mymodule
"""
from setuptools import setup

requirements = ['numpy>=1.0',
                # others
                ]

setup(
    name='mymodule', # the name of the module
    packages=['mymodule'], # the location of the module
    version='0.1',
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={
        'console_scripts':[
            'hello_world=mymodule.submod1:hello_world',
            'sky_sim=mymodule.sky_sim:generate_sky_pos',
        ]
    }
)