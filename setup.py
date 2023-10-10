#!/usr/bin/env python3

from setuptools import (
    setup, find_packages
)

# Project URL's
project_urls: dict = {
    "Tracker": "https://github.com/qtumproject/qtum-bip38/issues"
}

# README.md
with open("README.md", "r", encoding="utf-8") as readme:
    long_description: str = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements: list = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="qtum_bip38",
    version="v0.1.0",
    description="Python library for implementation of BIP38 for Qtum.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Meheret Tesfaye Batu",
    author_email="meherett@qtum.info",
    url="https://github.com/qtumproject/qtum-bip38",
    project_urls=project_urls,
    keywords=[
        "qtum", "bip38", "private-key", "pure-python", "encrypt", "decrypt", "passphrase", "wif", "bip-0038"
    ],
    python_requires=">=3.9,<4",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest>=7.4.0,<8",
            "pytest-cov>=4.1.0,<5"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
