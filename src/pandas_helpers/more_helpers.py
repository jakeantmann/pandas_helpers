"""Simple where for df.assign"""

# %% Imports
from dataclasses import dataclass, field
from typing import Any
from functools import partial
from collections.abc import Iterator, Container

import pandas as pd
import inspect

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

# %% Custom pipe functions
# Class approach (more pythonic)


@dataclass
class where(object):
    col_name: Any
    value: Any
    match: Any = None
    non_match: Any = None

    def __call__(self, df):
        """Run and output the inner function when the class is instantiated"""
        # Don't need to change this
        return self.inner_function(df)

    def inner_function(self, df):
        series = df[self.col_name]

        if self.match is None and self.non_match is None:
            raise Exception("'match' and 'non_match' cannot both be None")

        if self.match is not None:
            series = series.where(series == self.value, self.match)

        if self.non_match is not None:
            series = series.mask(series == self.value, self.non_match)

        return series


def where_closure(col_name, value, match=None, non_match=None):
    def inner_function(df):
        series = df[col_name]

        if match is None and non_match is None:
            raise Exception("'match' and 'non_match' cannot both be None")

        if match is not None:
            series = series.where(series == value, match)

        if non_match is not None:
            series = series.mask(series == value, non_match)

        return series

    return inner_function


# %%
df = pd.DataFrame(dict(
    a=[1, 2, 3, 4],
    b=[5, 6, 7, 8],
))

df1 = pd.DataFrame(
    {
        "x": [1, 5, 0, 4],
        "y": [5, pd.NA, 7, pd.NA],
        "z": [9, 10, 11, pd.NA],
    },
)

# %%
def is_col_test(obj):
    return hasattr(obj, "_is_col")

class Update(object):
    def __init__(self, col_name, *args, method=None, **kwargs):
        self.method = method
        self.col_name = col_name
        self.args = args
        self.kwargs = kwargs
        self._is_col = True

    def __call__(self, df):
        """Run and output the inner function when the class is instantiated"""
        # Don't need to change this
        return self.inner_function(df)

    def inner_function(self, df):
        return getattr(df[self.col_name], self.method)(*self.args, **self.kwargs)

    def __add__(self, other):
        if is_col_test(other):
            return lambda DF: self.__call__(DF) + other(DF)
        else:
            return lambda DF: self.__call__(DF) + other

    def __sub__(self, other):
        if is_col_test(other):
            return lambda DF: self.__call__(DF) - other(DF)
        else:
            return lambda DF: self.__call__(DF) - other

    def __rsub__(self, other):
        if is_col_test(other):
            return lambda DF: other(DF) - self.__call__(DF)
        else:
            return lambda DF: other - self.__call__(DF)

    def __radd__(self, other):
        if is_col_test(other):
            return lambda DF: other(DF) + self.__call__(DF)
        else:
            return lambda DF: other + self.__call__(DF)

    def combine_first(self, other):
        if is_col_test(other):
            return lambda DF: self.__call__(DF).combine_first(other(DF))
        else:
            return lambda DF: self.__call__(DF).combine_first(other)


# %%
col = partial(Update, method="__copy__")

# %%
df.assign(val = col("a") - col("b"))

# %%
df1.assign(val = col("y").combine_first(col("z")))

# %%
df.assign(val = col("a") - 10)

# %%
df.assign(val = 10 - col("a"))

# %%
df.assign(val = col("b") - 10 - col("a"))

# %%
df.assign(val = col("b") + 10 + col("a"))

df.assign(lambda DF: DF["a"])

# %%
@dataclass
class Boop(object):
    a: int

    def apply(self):
        return self.a

    def __mod__(self, other):
        return self.a * other

# %%
boop = Boop(4)

# %%
boop % 10

# %%
boop.apply()


# %%
col = partial(Update, method="__copy__")

add = partial(Update, method="__add__")
subtract = partial(Update, method="__sub__")
multiply = partial(Update, method="__mul__")
divide = partial(Update, method="__truediv__")
div = partial(Update, method="__floordiv__")
mod = partial(Update, method="__mod__")
absolute = partial(Update, method="__abs__")
power = partial(Update, method="__pow__")
cumsum = partial(Update, method="cumsum")
cumprod = partial(Update, method="cumprod")
cummin = partial(Update, "cummin")
cummax = partial(Update, "cummax")
dsum = partial(Update, method="sum", axis="columns")

# %% Coalesce
(
    df1
    .loc[:, ["y", "z", "x"]]
    .assign(coalesced_yzx = coalesce(["y", "z", "x"]))
    .rename_axis("COALESCE", axis="columns")
)

# %% Assign helpers
(
    df1
    .get(["y", "z", "x"])
    .assign(
        ADD_10 = add("x", 10),
        SUBTRACT_10 = subtract("x", 10),
        MULTIPLY_BY_3 = multiply("x", 3),
        DIVIDE_BY_3 = divide("x", 3),
        DIV_3 = div("x", 3),
        MOD_3 = mod("x", 3),
        ABS = absolute("x"),
        POWER_2 = power("x", 2),
        CUMSUM = cumsum("x"),
        CUMPROD = cumprod("x"),
        CUMMIN = cumsum("x"),
        CUMMAX = cumsum("x"),
        SUM_XY = dsum(["x", "y"]),
    )
    .rename_axis("ASSIGN HELPERS", axis="columns")
)
# %% Where
(
    df
    .assign(update_both = where("b", 6, "Match", "Not Match"))
    .assign(update_match = where("b", 6, "Match"))
    .assign(update_non_match = where("b", 6, non_match="Not Match"))
    .rename_axis("WHERE", axis="columns")
)

# %% Where: FAILS when updating neither
(
    df
    .assign(update_neither = where("b", 6))
)

# %%
def fn(y):
    def inner_function(x):
        return y + x
    return inner_function
# %%
fn(3)
# %%
z = fn(3)
# %%
df1[["x", "y"]].sum(axis="columns")

# %%
@dataclass


# %%
dsum = partial(DUpdate, method="sum", axis="columns")
cumprod = partial(DUpdate, method="cumprod")
# %%
df.assign(
    "SUM" = dsum(["a", "b"]),
    "CUMPROD" = dsum("b")
)
# %%
df.assign(val = lambda DF: DF["a"] + DF["b"])

# %%
df.assign(val = col("a") + col("b"))

# %%
df.assign(val = col("a") - col("b"))

# %%
col = partial(Update, method="__copy__")

df.assign(val = col("a") + col("b") - 10)

# %% There are no operators that we need that aren't already in dunders_series
import operator
import pandas as pd
series = pd.Series([1,2,3], name="beep")
# series = pd.Series([1j, 2j, 3j], name="beep")

dunders = sorted([i for i in dir(operator) if i.startswith("__")])
dunders_series = sorted([i for i in dir(series) if i.startswith("__")])

for method in dunders:
    attr_operator = getattr(operator, method)
    attr_type = type(getattr(operator, method))
    # if method in dunders_series:
    #     continue
    if "builtin_function_or_method" not in str(attr_type):
        continue
    try:
        # print(method, type(getattr(operator, method)))
        # print(f"{method} | {type(getattr(series, method))}")
        type(getattr(series, method))
    except AttributeError as e:
        print(f"{method} | {attr_type} | {e}")
        # print("------------------")
        # print(help(attr_operator))
    # print(method, type(getattr(operator, method)))
    # help(getattr(operator, method))

# %%
builtins = []
methods = []
properties = []

extra_methods = ["__class__", "__weakref__"]

max_len = max(len(i) for i in dunders_series)

for attr_string in dunders_series:
    attr = getattr(series, attr_string)
    type_string = str(type(attr))

    if "builtin" in type_string:
        builtins.append(attr_string)
    elif "method" in type_string:
        methods.append(attr_string)
    elif attr_string in extra_methods:
        pass
    elif callable(attr):
        raise Exception(f"The attr {attr_string} is not a builtin, method, or extra method")
    else:
        properties.append(attr_string)

print(
    f"{len(methods)    = }",
    f"{len(builtins)   = }",
    f"{len(properties) = }",
    sep = "\n"
)

# %% Write the code for others
for property_name in properties:
    txt = [
        f"\tdef {property_name}(self, DF):",
        f"\t\treturn DF[self.col].{property_name}",
        ""
    ]

    print(*txt, sep="\n")

# %% Write the code for methods
for method in methods:
    if method in ["__init__"]:
        continue

    params = inspect.signature(getattr(series, method)).parameters

    param_names = params.keys()
    param_names_str = ", ".join(param_names)

    params_with_default_args = [str(value) for value in params.values()]
    params_with_default_args_str = ", ".join(params_with_default_args)

    if "other" in params:
        print(f"----- {params} -----")
        params_str_DF = param_names_str.replace("other", "other(DF)")

        text = [
            f"    def {method}(self, {params_with_default_args_str}):",
            f"        if is_col_test(other):",
            f"            return lambda DF: self.__call__(DF).{method}({params_str_DF})",
            f"        else:",
            f"            return lambda DF: self.__call__(DF).{method}({param_names_str})",
            f"",
        ]
    else:
        params_with_default_args = ", ".join([str(value) for value in inspect.signature(fn).parameters.values()])
        param_names = ", ".join(inspect.signature(fn).parameters.keys())

        text = [
            f"    def {method}(self, {params_with_default_args}):",
            f"        return lambda DF: self.__call__(DF).{method}({param_names})",
            f"",
        ]

    print(*text, sep="\n")

# %% Write the code for builtins
checked_builtins = [
    '__format__',
    '__init_subclass__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__subclasshook__'
]

for builtin_name in builtins:
    if builtin_name not in checked_builtins:
        raise Exception("There's a builtin not accounted")

# %% Write the code for extra methods
for method in extra_methods:
    if method != "__weakref__":
        params = inspect.signature(series.__class__).parameters

        param_names = params.keys()
        param_names_str = ", ".join(param_names)

        params_with_default_args = [str(value) for value in params.values()]
        params_with_default_args_str = ", ".join(params_with_default_args)

    if method == "__class__":
        params_str_DF = param_names_str.replace("data", "data(DF)")

        text = [
            f"    def {method}(self, {params_with_default_args_str}):",
            f"        if is_col_test(data):",
            f"            return lambda DF: self.__call__(DF).{method}({params_str_DF})",
            f"        else:",
            f"            return lambda DF: self.__call__(DF).{method}({param_names_str})",
            f"",
        ]
    elif method == "__weakref__":
        text = [
            f"    def {method}(self):",
            f"        return lambda DF: self.__call__(DF).{method}()",
            f"",
        ]
    else:
        raise Exception("{method} is in the list of extra_methods, but doesn't have a function builder")

    print(*text, sep="\n")
