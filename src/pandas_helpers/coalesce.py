"""Implements the tidyverse 'coalesce' function in python."""

from collections.abc import Iterator
from dataclasses import dataclass

import pandas as pd


@dataclass
class coalesce(object): # noqa D400
    """Find the first non-missing element.

    See https://dplyr.tidyverse.org/reference/coalesce.html
    """

    cols: Iterator

    def __call__(self, df: pd.DataFrame):
        """Implement the inner function when object is called."""
        # Don't need to change this
        return self.inner_function(df)

    def inner_function(self, df):
        """Inner function."""

        msg = "'{col}' is not in the DataFrame, so function 'coalesce' fails."

        try:
            output = df[self.cols[0]]
        except IndexError:
            raise IndexError("No cols were supplied to coalesce")
        except KeyError:
            raise KeyError(msg.format(col=self.cols[0]))

        for col in self.cols[1:]:
            try:
                output = output.combine_first(df[col])
            except KeyError:
                raise KeyError(msg.format(col=col))

        return output

# TODO Wrong magic comment
# TODO Fix docstrings
# - Parameters
# - Returns
# - Multiline final quotes
# - Raises
# TODO Change max line length to 120
