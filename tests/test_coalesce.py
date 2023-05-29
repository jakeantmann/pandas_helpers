"""Test the coalesce class."""

from contextlib import nullcontext as does_not_raise

import pandas as pd
import pytest

from pandas_helpers.coalesce import coalesce

df1 = pd.DataFrame(
    {
        "x": [1, 2, 3, 4],
        "y": [5, pd.NA, 7, pd.NA],
        "z": [9, 10, 11, pd.NA],
    },
)

df2 = df1.replace(pd.NA, None)


@pytest.mark.parametrize(
    "df,cols,expectation",
    [
        (df1, ["y", "z", "x"], [5, 10, 7, 4]),
        (df1, ["y", "x", "z"], [5, 2, 7, 4]),
        (df1, ["y", "z"], [5, 10, 7, pd.NA]),
        (df2, ["y", "z", "x"], [5, 10, 7, 4]),
        (df2, ["y", "x", "z"], [5, 2, 7, 4]),
        (df2, ["y", "z"], [5, 10, 7, None]),
    ],
)
def test_coalesce(df, cols, expectation):
    """Test coalesce."""
    assert df.assign(a=coalesce(cols))["a"].to_list() == expectation


@pytest.mark.parametrize(
    "df,cols,expectation",
    [
        (df1, [], pytest.raises(IndexError)),
        (df1, ["b"], pytest.raises(KeyError)),
        (df1, ["b", "x"], pytest.raises(KeyError)),
        (df1, ["x", "b"], pytest.raises(KeyError)),
        (df1, ["x"], does_not_raise()),
        (df1, ["y", "x"], does_not_raise()),
    ],
)
def test_coalesce_errors(df, cols, expectation):
    """Test coalesce errors."""
    with expectation:
        df.assign(a=coalesce(cols))

# TODO string literal overuse (x,y,z)
# TODO single quotes preferred?!
# TODO docstrings
# - Parameters
# TODO assert
#
