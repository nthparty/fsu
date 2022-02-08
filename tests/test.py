from sfu import *
import pytest


@pytest.mark.parametrize(
    "uri, expected",
    [
        ("snow://abc:xyz:123@db/table",
         {"user": "abc", "password": "xyz", "account": "123"}),
        ("snow://abc:xyz@db/table", {"user": "abc", "password": "xyz"})
    ]
)
def test_credentials(uri: str, expected: dict):
    test_object = sfu(uri)

    cred = test_object.credentials()
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
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh",
            False,
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
            True,
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
            False,
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh", "p": "p"}
        )
    ]
)
def test_configuration(uri: str, safe: bool, expected: dict):
    test_object = sfu(uri)

    conf = test_object.configuration(safe=safe)
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
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh",
            False,
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
            True,
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
            False,
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh", "p": "p"}
        )
    ]
)
def test_connection(uri: str, safe: bool, expected: dict):
    test_object = sfu(uri)

    conn = test_object.for_connection(safe)
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
    test_object = sfu(uri)

    db = test_object.for_db()
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
    test_object = sfu(uri)

    wh = test_object.for_warehouse()
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
    test_object = sfu(uri)

    tb = test_object.for_table()
    assert tb == expected


@pytest.mark.parametrize(
    "uri, expected",
    [
        ("snow://abc:xyz:123@db/tb", "snow://abc:xyz:123@db/tb"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh",
         "snow://abc:xyz:123@db/tb?warehouse=wh"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
         "snow://abc:xyz:123@db/tb?warehouse=wh&p=p")
    ]
)
def test_to_string(uri: str, expected: str):
    test_object = sfu(uri)

    tb = test_object.to_string()
    assert tb == expected


# Test that sfu class can handle property value changes
@pytest.mark.parametrize(
    "uri, edit_key, edit_val, expected",
    [
        ("snow://abc:xyz:123@db/table", "password", "asdf",
         {"user": "abc", "password": "asdf", "account": "123"}),
        ("snow://abc:xyz@db/table", "user", "DEF",
         {"user": "DEF", "password": "xyz"})
    ]
)
def test_credentials_edit(uri: str, edit_key: str, edit_val: str, expected: dict):
    test_object = sfu(uri)

    setattr(test_object, edit_key, edit_val)

    cred = test_object.credentials()
    assert cred == expected


@pytest.mark.parametrize(
    "uri, safe, edit_key, edit_val, expected",
    [
        (
            "snow://abc:xyz:123@db/tb",
            True,
            "database",
            "db2",
            {"user": "abc", "password": "xyz", "account": "123", "database": "db2"}
        ),
        (
            "snow://abc:xyz:123@db/tb",
            False,
            "database",
            "db2",
            {"user": "abc", "password": "xyz", "account": "123", "database": "db2"}
        ),
        (
            "snow://abc:xyz@db/tb",
            True,
            "user",
            "jkl",
            {"user": "jkl", "password": "xyz", "database": "db"}
        ),
        (
            "snow://abc:xyz@db/tb",
            False,
            "user",
            "jkl",
            {"user": "jkl", "password": "xyz", "database": "db"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh",
            True,
            "warehouse",
            "new_wh",
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "new_wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh",
            False,
            "warehouse",
            "new_wh",
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "new_wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
            True,
            "account",
            "456",
            {"user": "abc", "password": "xyz", "account": "456",
                "database": "db", "warehouse": "wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
            False,
            "p",
            "np",
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh", "p": "np"}
        )
    ]
)
def test_configuration_edit(uri: str, safe: bool, edit_key: str, edit_val: str, expected: dict):
    test_object = sfu(uri)

    setattr(test_object, edit_key, edit_val)

    conf = test_object.configuration(safe=safe)
    assert conf == expected


@pytest.mark.parametrize(
    "uri, safe, edit_key, edit_val, expected",
    [
        (
            "snow://abc:xyz:123@db/tb",
            True,
            "database",
            "db2",
            {"user": "abc", "password": "xyz", "account": "123", "database": "db2"}
        ),
        (
            "snow://abc:xyz:123@db/tb",
            False,
            "password",
            "very_secure",
            {"user": "abc", "password": "very_secure",
                "account": "123", "database": "db"}
        ),
        (
            "snow://abc:xyz@db/tb",
            True,
            "user",
            "hij",
            {"user": "hij", "password": "xyz", "database": "db"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh",
            True,
            "warehouse",
            "new_wh",
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "new_wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh",
            False,
            "warehouse",
            "new_wh",
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "new_wh"}
        ),
        (
            "snow://abc:xyz:123@db/tb?warehouse=wh&p=p",
            False,
            "p",
            "np",
            {"user": "abc", "password": "xyz", "account": "123",
                "database": "db", "warehouse": "wh", "p": "np"}
        )
    ]
)
def test_connection(uri: str, safe: bool, edit_key: str, edit_val: str, expected: dict):
    test_object = sfu(uri)

    setattr(test_object, edit_key, edit_val)

    conn = test_object.for_connection(safe)
    assert conn == expected


@pytest.mark.parametrize(
    "uri, edit_key, edit_val, expected",
    [
        ("snow://abc:xyz:123@db/tb", "database",
         "new_db", "snow://abc:xyz:123@new_db/tb"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh", "user", "DEF",
         "snow://DEF:xyz:123@db/tb?warehouse=wh"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh", "password", "",
         "snow://abc::123@db/tb?warehouse=wh"),
        ("snow://abc:xyz:123@db/tb?warehouse=wh&p=p", "p", "np",
         "snow://abc:xyz:123@db/tb?warehouse=wh&p=np")
    ]
)
def test_to_string(uri: str, edit_key: str, edit_val: str, expected: str):
    test_object = sfu(uri)

    setattr(test_object, edit_key, edit_val)

    tb = test_object.to_string()
    assert tb == expected
