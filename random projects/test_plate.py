from plate import is_valid

def test_is_valid_starts_with_two_letters():
    assert is_valid("  AAA222") == True
    assert is_valid("CS50") == True
    assert is_valid("50") == False

def test_is_valid_max_6_and_min_2():
    assert is_valid("OUTATIME") == False
    assert is_valid('HELLO') == True

def test_is_valid_no_punctuations():
    assert is_valid("!NOTVD") == False
    assert is_valid('HELLO,') == False

def test_is_valid_no_numbers_between_plate():
    assert is_valid("CS50P") == False
    assert is_valid("AAA22A") == False
    assert is_valid("PI3.14") == False

def test_is_valid_first_num_cant_be_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS5") == True
