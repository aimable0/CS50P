from jar import Jar
import pytest

# initiate an instance to test with.
jar = Jar(15)


def test_jar_deposit():
    jar.deposit(5)


def test_jar_with_more_than_max():
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_str():
    assert str(jar) == "🍪🍪🍪🍪🍪"
    # jar = Jar()
    # assert str(jar) == ""
    # jar.deposit(1)
    # assert str(jar) == "🍪"
    # jar.deposit(11)
    # assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_jar_with_withdraw():
    jar.withdraw(3)


def test_jar_with_withdraw_than_min():
    with pytest.raises(ValueError):
        jar.withdraw(3)


# test attributes


def test_jar_size():
    assert jar.size == 2


def test_jar_capacity():
    assert jar.capacity == 15
