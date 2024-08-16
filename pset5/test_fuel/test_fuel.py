from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    

def test_value():
      with pytest.raises(ValueError):
          convert("three/four")

def test_zero():
      with pytest.raises(ZeroDivisionError):
          convert("5/0")

def test_gauge():
     assert gauge(75) == "75%"
     assert gauge(1) == "E"
     assert gauge(99) == "F"
     assert gauge(25) == "25%"
