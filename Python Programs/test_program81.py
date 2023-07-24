import pytest
import program81


@pytest.mark.testnumber
def test_add():
    assert program81.add(10, 20) == 30
    assert program81.add(1, 2) == 3
    assert program81.add(1, 4) == 6


@pytest.mark.testnumber
def test_sub():
    assert program81.sub(10, 20) == -10
    assert program81.sub(1, 2) == 3


@pytest.mark.testnumber
def test_product():
    assert program81.product(10, 20) == 200
    assert program81.product(5, 6) == 40


@pytest.mark.testnumber
def test_mod():
    assert program81.mod(20, 10) == 0
    assert program81.mod(5, 2) == 3


@pytest.mark.teststring
def test_add_strings():
    assert program81.add("CHAT ", "GPT") == "CHAT GPT"
    result = program81.add("KL-", "CSE")
    print(result)
    assert type(result) is str
    assert "HOD" in result
    assert type(result) is not int
    assert "KLEF" not in result
