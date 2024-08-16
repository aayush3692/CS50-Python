from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hii") == 20
    assert value("Good morning, sir!") == 100
    assert value("Have a nice day, sir!") == 20
