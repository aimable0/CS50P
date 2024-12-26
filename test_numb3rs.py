from numb3rs import validate

def test_validate_int_valid_input():
    assert validate('1.2.3.4') == True
    assert validate('124.255.255.255') == True
    assert validate('0.0.0.0') == True

def test_validate_int_invalid_input():
    assert validate('256.0.0') == False
    assert validate('255.257.0.1') == False
    assert validate('-12.12.2.1') == False

def test_validate_non_int_input():
    assert validate('love') == False
    assert validate('') == False
    assert validate('124.123.no.no') == False
    assert validate('no.no.no.no') == False