# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

from setuptools import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="HTMLtoPDF",
    packages=["HTMLtoPDF"],
    entry_points={
        "console_scripts": ['HTMLtoPDF = HTMLtoPDF.main:main']
    },
    version='0.0.1',
    description="Python app to convert articles on the web to pdf",
    long_description=long_descr,
    author="Dmitry Filosofov",
    author_email="filosofov.dmitry@gmail.com",
    url="https://github.com/polyx/HTMLtoPDF",
    data_files=[('css', ['HTMLtoPDF/css/bootstrap.css'])]
)
