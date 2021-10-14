from sfu import *
import pytest


@pytest.mark.parametrize(
    "uri, expected",
    [
        ("snow://abc:xyz:123@db/table", {"user": "abc", "password": "xyz", "account": "123"}),
        ("snow://abc:xyz@db/table", {"user": "abc", "password": "xyz"})
    ]
)
def test_credentials(uri: str, expected: dict):

    cred = credentials(uri)
    assert cred == expected


@pytest.mark.parametrize(
    "uri, safe, expected",
    [
        (
                "snow://abc:xyz:123@db/tb",
                True,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db"}
        ),
        (
                "snow://abc:xyz:123@db/tb",
                False,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db"}
        ),
        (
                "snow://abc:xyz@db/tb",
                True,
                {"user": "abc", "password": "xyz", "database": "db"}
        ),
        (
                "snow://abc:xyz@db/tb",
                False,
                {"user": "abc", "password": "xyz", "database": "db"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh",
                True,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh",
                False,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
                True,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
                False,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh", "p": "p"}
        )
    ]
)
def test_configuration(uri: str, safe: bool, expected: dict):

    conf = configuration(uri, safe=safe)
    assert conf == expected


@pytest.mark.parametrize(
    "uri, safe, expected",
    [
        (
                "snow://abc:xyz:123@db/tb",
                True,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db"}
        ),
        (
                "snow://abc:xyz:123@db/tb",
                False,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db"}
        ),
        (
                "snow://abc:xyz@db/tb",
                True,
                {"user": "abc", "password": "xyz", "database": "db"}
        ),
        (
                "snow://abc:xyz@db/tb",
                False,
                {"user": "abc", "password": "xyz", "database": "db"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh",
                True,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh",
                False,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
                True,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh"}
        ),
        (
                "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
                False,
                {"user": "abc", "password": "xyz", "account": "123", "database": "db", "warehouse": "wh", "p": "p"}
        )
    ]
)
def test_connection(uri: str, safe: bool, expected: dict):

    conn = for_connection(uri, safe)
    assert conn == expected


@pytest.mark.parametrize(
    "uri, expected",
    [
        ("snow://abc:xyz:123@db/tb", "db"),
        ("snow://abc:xyz@db/tb", "db"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh", "db"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh&p=p", "db")
    ]
)
def test_for_db(uri: str, expected: str):

    db = for_db(uri)
    assert db == expected


@pytest.mark.parametrize(
    "uri, expected",
    [
        ("snow://abc:xyz:123@db/tb", None),
        ("snow://abc:xyz@db/tb", None),
        ("snow://abc:xyz:123@db/tb?warehouse=wh", "wh"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh&p=p", "wh")
    ]
)
def test_for_warehouse(uri: str, expected: [str, None]):

    wh = for_warehouse(uri)
    assert wh == expected


@pytest.mark.parametrize(
    "uri, expected",
    [
        ("snow://abc:xyz:123@db/tb", "tb"),
        ("snow://abc:xyz@db/tb", "tb"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh", "tb"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh&p=p", "tb")
    ]
)
def test_for_table(uri: str, expected: str):

    tb = for_table(uri)
    assert tb == expected
