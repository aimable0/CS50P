from bank import check_greeting
    # this is a space

# this is comment
def test_check_greeting_mixed():
    # This is a comment
    assert check_greeting("Hello, Newman") == "$0"
    assert check_greeting("Hello") == "$0"

def test_check_greeting_with_puncs():
    assert check_greeting("How you doing?") == "$20"
    assert check_greeting("What's happening?") == "$100"

def test_check_greeting_all_capital():
    assert check_greeting("HELLO") == "$0"

...
