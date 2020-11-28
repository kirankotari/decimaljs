from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
reqs = []

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    read_lines = f.readlines()
    reqs = [each.strip() for each in read_lines]

setup(
    name="decimaljs",
    version="1.0.0",
    description="An arbitrary-precision Decimal type for JavaScript to Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirankotari/decimaljs",
    author="Kiran Kumar Kotari",
    author_email="kirankotari@live.com",
    install_requires=reqs,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="decimal.js decimal decimaljs",
    packages=find_packages(where=".", exclude=["tests", "data"]),
    include_package_data=True,
)
