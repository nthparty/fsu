===
sfu
===

Snowflake URI utility library that supports extraction of Snowflake configuration data and method parameters from Snowflake resource URIs.

|readthedocs| |actions|

.. |readthedocs| image:: https://readthedocs.org/projects/sfu/badge/?version=latest
   :target: https://sfu.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/nthparty/sfu/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/nthparty/sfu/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

Purpose
-------
When applications that employ the `Snowflake Python SDK <https://docs.snowflake.com/en/user-guide/python-connector.html>`_ must work with resources that are spread across multiple accounts, it can be useful to tie Snowflake configuration information (both credentials and resource data) directly tot associated Snowflake resources (*e.g.*, by including the  configuration data within URIs). This library provides methods that extract Snowflake configuration data and method  parameters from URIs, offering a succint syntax for passing (directly into Snowflake methods) configuration data and/or resource names that are included within URIs.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install sfu

The library can be imported in the usual ways::

    import sfu
    from sfu import *

The library provides methods for extracting configuration data (credentials and non-credentials) from URIs, as in the examples below::

    import sfu
    import snowflake.connector

    # Create a connector client given a URI (for a table in some snowflake database) that
    # includes credentials (a username 'ABC', a password 'XYZ', and an associated account 
    # 'UVW').
    conn = connector.connect(**sfu.credentials("snow://ABC:XYZ:UVW@DATABASE"))

    # It can also be useful to bind a connection to some database and some data processing 
    # warehouse, so you don't need to execute cursor commands later. The following will 
    # return a connector client that is configured against DATABASE, using WH for data 
    # processing.
    uri = "snow://ABC:XYZ:UVW@DATABASE/TABLE@warehouse=WH"
    c = connector.connect(**sfu.for_connection(uri))
    cs = c.cursor()
    cs.execute(f"SELECT col1,col2 FROM {sfu.for_table(uri)}")

    # Note that this is equivalent to the following:
    c = connector.connect(**sfu.credentials(uri))
    cs = c.cursor()
    cs.execute(f"USE DATABASE {sfu.for_db(uri)}")
    cs.execute(f"USE WAREHOUSE {sfu.for_warehouse(uri)}")
    cs.execute(f"SELECT col1,col2 FROM {sfu.for_table(uri)}")

Documentation
-------------
.. include:: toc.rst

The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org/>`_::

    cd docs
    python -m pip install -r requirements.txt
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. ../setup.py && make html

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `pytest <https://pytest.org>`_::

  python -m pip install pytest pytest-cov .
  python -m pytest --cov=sfu tests/test.py

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

  python -m pip install pylint
  pylint sfu

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
