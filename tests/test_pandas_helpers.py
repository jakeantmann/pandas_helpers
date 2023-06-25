"""Test pandas helpers."""

from contextlib import nullcontext as does_not_raise

import pytest

def my_sum(var1, var2):
    return var1 + var2

@pytest.mark.parametrize(
    "var1,var2,expectation",
    [
        (1, 1, 2),
        (1, 2, 3),
    ],
)
def test_my_sum(var1, var2, expectation):
    """Test my_sum."""
    assert my_sum(var1, var2) == expectation


@pytest.mark.parametrize(
    "var1,var2,expectation",
    [
        (1, "a", pytest.raises(TypeError)),
        (1, 2, does_not_raise())
    ],
)
def test_my_sum_errors(var1, var2, expectation):
    """Test coalesce errors."""
    with expectation:
        my_sum(var1, var2)

# TODO string literal overuse (x,y,z)
# TODO single quotes preferred?!
# TODO docstrings
# - Parameters
# TODO assert
#
