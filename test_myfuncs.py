import pytest

from myfuncs import add, sub, multiply, divide, power, modulo

@pytest.mark.parametrize(
    "a,b,res",
    [
        (0, 0, 0),
        (0, 42, 42),
        (42, 0, 42),
        (42, -42, 0),
        (-42, 42, 0),
    ]
)
def test_add(a, b, res):
    assert add(a, b) == res


@pytest.mark.parametrize(
    "a,b,res",
    [
        (0, 0, 0),
        (0, 42, -42),
        (42, 0, 42),
        (42, 42, 0),
        (42, -42, 84),
        (-42, 42, -84),
    ]
)
def test_sub(a, b, res):
    assert sub(a, b) == res


@pytest.mark.parametrize(
    "a,b,res",
    [
        (0, 0, 0),
        (0, 42, 0),
        (42, 0, 0),
        (42, 1, 42),
        (1, 42, 42),
        (-1, 42, -42),
    ]
)
def test_multiply(a, b, res):
    assert multiply(a, b) == res


@pytest.mark.parametrize(
    "a,b,res",
    [
        (0, 0, None),
        (0, 42, 0),
        (42, 0, None),
        (42, 1, 42),
        (1, 2, 0.5),
        (-1, 2, -0.5),
    ]
)
def test_divide(a, b, res):
    assert divide(a, b) == res


@pytest.mark.parametrize(
    "a,b,res",
    [
        (0, 0, 1),
        (0, 2, 0),
        (1, 2, 1),
        (2, 0, 1),
        (2, 1, 2),
        (2, 2, 4),
        (2, -1, 0.5),
    ]
)
def test_power(a, b, res):
    assert power(a, b) == res

@pytest.mark.parametrize(
    "a,b,res",
    [
        (0, 0, None),
        (0, 42, 0),
        (42, 0, None),
        (42, 1, 0),
        (1, 42, 1),
        (10, 3, 1),
        (10, 5, 0),
    ]
)
def test_modulo(a, b, res):
    assert modulo(a, b) == res
