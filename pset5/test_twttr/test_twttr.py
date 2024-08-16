from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("hEy") == "hy"
    assert shorten("tIp") == "tp"
    assert shorten("1a2be") == "12b"
    assert shorten("Hey!") == "Hy!"
