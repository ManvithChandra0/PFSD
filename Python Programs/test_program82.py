# program to demonstrate skipping test functions

import pytest
import program81


@pytest.mark.skip(reason="I hate this function to execute")
def test_add():
    assert program81.add(10, 20) == 30
    assert program81.add(1, 2) == 3
    assert program81.add(1, 4) == 6


@pytest.mark.skip(reason="I don't want to execute this function")
def test_sub():
    assert program81.sub(10, 20) == -10
    assert program81.sub(1, 2) == 3


@pytest.mark.teststring
def test_add_strings():
    assert program81.add("CHAT ", "GPT") == "CHAT GPT"
    result = program81.add("KL-", "CSE")
    print(result)
    assert type(result) is str
    assert "HOD" in result
    assert type(result) is not int
    assert "KLEF" not in result
