from working import convert
import pytest

def test_no_match():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("22:30 to 08:50")

def test_outof_range():
    with pytest.raises(ValueError):
        convert("00:00 AM to 17:30 PM")
    with pytest.raises(ValueError):
        convert("09:60 AM to 17:80 PM")

def test_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
