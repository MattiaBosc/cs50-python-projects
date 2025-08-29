from um import count

def test_inside_words():
    assert count("") == 0
    assert count("yummy") == 0
    assert count("  um  ") == 1
    assert count("um... album") == 1

def test_case_sensitivity():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("uM") == 1

def test_multiple_occurrences():
    assert count("UM... um, I don't know") == 2
    assert count("Um, I'll take, um, an umbrella") == 2
