# program to demonstrate Pytest Parametrized Tests

import program81
import pytest


@pytest.mark.parametrize('num1,num2,result', [
    (7, 3, 10),  # first tuple
    ('PFSD', '-MSWD', 'PFSD-MSWD'),  # second tuple
    (10.5, 25.5, 36),  # third tuple
    ("HOD", "3", "HODSURYA"),  # fourth tuple
    ("ANVESH", "-MALE", "ANVESHMALE"),  # fifth tuple
])
def test_add(num1, num2, result):
    assert program81.add(num1, num2) == result
