=====
flats
=====

Python library for common functionalities related to flattening nested instances of container types.

|pypi| |travis| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/flats.svg
   :target: https://badge.fury.io/py/flats
   :alt: PyPI version and link.

.. |travis| image:: https://travis-ci.com/lapets/flats.svg?branch=master
    :target: https://travis-ci.com/lapets/flats

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/flats/badge.svg?branch=master
   :target: https://coveralls.io/github/lapets/flats?branch=master

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install flats

The library can be imported in the usual ways::

    import flats
    from flats import flats

A usage example is provided  below::

    >>> from flats import flats
    >>> list(flats([[1, [2, 3]], [4, 5, 6, 7]]))
    [1, 2, 3, 4, 5, 6, 7]

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configution details)::

    nosetests

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python flats/flats.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint flats

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
Beginning with version 0.1.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
