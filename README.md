# fsu
Snowflake URI utility library that supports extraction of Snowflake configuration data and method parameters from Snowflake resource URIs.


## Purpose

When applications that employ the [Snowflake Python SDK](https://docs.snowflake.com/en/user-guide/python-connector.html) 
must work with resources that are spread across multiple accounts, it can be useful to tie Snowflake configuration 
information (both credentials and resource data) directly tot associated Snowflake resources (e.g., by including the 
configuration data within URIs). This library provides methods that extract Snowflake configuration data and method 
parameters from URIs, offering a succint syntax for passing (directly into Snowflake methods) configuration data and/or 
resource names that are included within URIs.

## Package Installation and Usage

The package is available on PyPI:

```shell
python -m pip install sfu
```

The library can be imported in the usual ways:

```python
import sfu
from sfu import *
```

The library provides methods for extracting configuration data (credentials and non-credentials) from URIs, as in the 
examples below:

```python
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
```

## Testing and Conventions

All unit tests are executed when using `pytest`:

```shell
pytest tests/test.py
```

## Contributions

In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

## Versioning

The version number format for this library and the changes to the library associated with version number increments 
conform with [Semantic Versioning 2.0.0](https://semver.org/#semantic-versioning-200).
