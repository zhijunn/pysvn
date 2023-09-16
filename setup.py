# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pysubversion",
    version="1.0.2",
    keywords=["svn", "pysvn", "subversion"],
    description="Svn for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD License",
    url="https://github.com/zhijunn/pysvn",
    author="Ryan Bender, Forked by Zhijunn.",
    author_email="zhijunn@yeah.net",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    # install_requires = ["codecs"]
)
