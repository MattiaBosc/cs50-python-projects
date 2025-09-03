from numb3rs import validate

def test_length():
    assert validate("1.1.1.1.1") == False
    assert validate("1.1") == False
    assert validate(" ") == False
    assert validate("1...1") == False

def test_other_characters():
    assert validate("cat.dog.None.1") == False
    assert validate("2$.4().2.1!") == False
    assert validate("4,6.5,9.8^.1") == False
    assert validate("1 . 4. 3 .5 ") == False

def test_outof_range():
    assert validate("543.1.1.1") == False
    assert validate("5.1234.1.1") == False
    assert validate("3.1.456.1") == False
    assert validate("5.4.6.1432") == False
    assert validate("-2.0.1.-6") == False
