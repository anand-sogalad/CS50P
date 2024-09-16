from tokenize import single_quoted

import pytest

from calculator import square


# this is not a good test
# def test_square():
#     for i in [-3, -1, 0, 1, 3, "anand", "sogalad", 0.3, -0.2, 0.6]:
#         if isinstance(i, str):
#             with pytest.raises(TypeError):
#                 square(i)
#             continue
#         assert square(i) == pow(i, 2), "Test Failed"


# tests must be simple and isolated
# self explanatory names
def test_square_int():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9


def test_square_neg_int():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9


def test_square_float():
    assert square(1.2) == 1.44
    assert square(2.5) == 6.25
    assert square(3.6) == 12.96


def test_square_neg_float():
    assert square(-1.2) == 1.44
    assert square(-2.5) == 6.25
    assert square(-3.6) == 12.96


def test_square_zero():
    assert square(0) == 0


def test_square_str():
    with pytest.raises(TypeError):
        square("anand")
