import pytest

from mod import some_variant2


@pytest.fixture
def summ_op():
    print(f"1 Start SUM OPERATION testing 1")


@pytest.fixture
def diff():
    print(f"2 Start DIFF OPERATION testing 2")


@pytest.fixture
def multiple():
    print(f"3 Start MULTIPLE OPERATION testing 3")


@pytest.fixture
def division():
    print(f"4 Start DIVISION OPERATION testing 4")


def test_sum_1(summ_op):
    assert some_variant2.sum(2, 3) > 0


def test_sum_2(summ_op):
    assert some_variant2.sum(2, 3) == 5


def test_difference_1(diff):
    assert some_variant2.difference(6, 2) == 4


def test_difference_2(diff):
    assert some_variant2.difference(2, 3) == -1


def test_difference_2(diff):
    assert some_variant2.difference(2, 3) < 0


def test_multiplication_3(multiple):
    assert some_variant2.multiplication(4, 5) == 20


def test_division_4(division):
    assert some_variant2.division(10, 2) == 5


def test_division_zero_4(division):
    assert some_variant2.division(5, 0) == 0
