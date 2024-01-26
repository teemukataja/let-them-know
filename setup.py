"""Install module."""

from setuptools import setup

setup(
    name="let_them_know",
    version="0.1.0",
    license="Public Domain",
    author="Teemu Kataja",
    author_email="",
    description="Script for updating RocketChat status based on Zimbra calendar appointments",
    long_description="",
    packages=["let_them_know", "let_them_know/zimbra", "let_them_know/rocketchat"],
    entry_points={"console_scripts": ["ltk=let_them_know.main:main"]},
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Public Domain",
        "Programming Language :: Python :: 3.12",
    ],
    install_requires=["requests"],
)
