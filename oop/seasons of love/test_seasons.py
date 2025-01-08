from datetime import date
from seasons import get_minutes, get_birth_date
import pytest


def test_get_minutes():
    assert (
        get_minutes(date.fromisoformat("2023-01-08"))
        == "One million, fifty-two thousand, six hundred and forty minutes"
    )
    assert (
        get_minutes(date.fromisoformat("2022-01-08"))
        == "One million, five hundred and seventy-eight thousand, two hundred and forty minutes"
    )


def test_get_birth_date_with_invalids():
    with pytest.raises(SystemExit):
        get_minutes("2012-16-08")
