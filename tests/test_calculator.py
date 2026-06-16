import pytest
from calculator import add, subtract, divide, modulo, sqrt, power


# --- add() ---
def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5


# --- subtract() ---
def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_zero():
    assert subtract(5, 0) == 5


# --- divide() ---
def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("a", 2)


# --- modulo() ---
def test_modulo_normal():
    assert modulo(10, 3) == 1


def test_modulo_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)