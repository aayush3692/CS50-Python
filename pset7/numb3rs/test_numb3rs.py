from numb3rs import validate

def test_alphabets():
    assert validate("cat") == False
    assert validate("a.b.c.d") == False

def test_digits():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("125.265.422.5") == False
