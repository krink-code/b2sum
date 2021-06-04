
# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


from setuptools import setup


setup(
    name = "b2sum",
    packages = ["b2sum"],
    entry_points = {
        "console_scripts": ['b2sum = b2sum.b2sum:main']
        },
    version = '0.0.1',
    description = "b2sum blake2",
    long_description = "Python command line tool for b2sum.",
    author = "Karl Rink",
    author_email = "karl@rink.us",
    url = "https://github.com/karlrink/b2sum",
    install_requires = [ ]
    )


