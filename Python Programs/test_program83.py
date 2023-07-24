# program to demonstrate pytest fixture

import pytest


@pytest.fixture()
def setup():
    print("Once Before Every Method")
    yield
    print("Once After Every Method")


def testmethod1(setup):
    print("This is Test Method 1")


def testmethod2(setup):
    print("This is Test Method 2")


def testmethod3(setup):
    print("This is Test Method 3")
