from seasons import convert
import pytest

def test_convert():
    with pytest.raises(SystemExit):
        convert("January 1, 1998")
    with pytest.raises(SystemExit):
        convert("2015-3-1")
    with pytest.raises(SystemExit):
        convert("2023/09/14")
    with pytest.raises(ValueError):
        convert("2018-45-96")
    assert convert("2023-05-05") == 366
    assert convert("2024-05-04") == 1
