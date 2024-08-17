from plates import is_valid

def test_length():
    assert is_valid("CSC500") == True
    assert is_valid("G") == False
    assert is_valid("0ELLORLD") == False

def test_letters():
    assert is_valid("HR4500") == True
    assert is_valid("45t0t") == False


def test_numbers():
    assert is_valid("R0WW") == False
    assert is_valid("PI3.14") == False
    assert is_valid("QWERTY") == True
    assert is_valid("") == False

def test_digits():
    assert is_valid("QWE456") == True
    assert is_valid("123456") == False
    assert is_valid("Hii$!!") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
