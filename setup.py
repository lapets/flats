from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read().replace(".. include:: toc.rst\n\n", "")

# The lines below can be parsed by `docs/conf.py`.
name = "flats"
version = "0.3.0"

setup(
    name=name,
    version=version,
    packages=[name,],
    install_requires=[],
    license="MIT",
    url="https://github.com/lapets/flats",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Minimal library that enables flattening of nested "+\
                "instances of container types.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
)
