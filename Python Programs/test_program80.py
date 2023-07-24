import program80
import pytest


def test_add():
    assert program80.add(1, 2) == 3
    assert program80.add(10, 20) == 40


def test_product():
    assert program80.product(1, 2) == 2
    assert program80.product(3, 4) == 10


def test_sub():
    assert program80.sub(1, 2) == -1
    assert program80.sub(10, 20) == 30


def test_mod():
    assert program80.mod(20, 4) == 0
    assert program80.mod(10, 20) == 40
