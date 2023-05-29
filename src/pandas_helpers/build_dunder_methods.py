
# %%
import operator
import inspect

import pandas as pd

# %%
series = pd.Series([1,2,3], name="beep")

# %%
dunders = sorted([i for i in dir(operator) if i.startswith("__")])
dunders_series = sorted([i for i in dir(series) if i.startswith("__")])

exclusion_list = [
    "__concat__",
    "__iconcat__",
    "__ilshift__",
    "__imatmul__",
    "__index__",
    "__inv__",
    "__irshift__",
    "__lshift__",
    "__not__",
    "__rshift__",
]

# %%
for method in dunders:
    if method in exclusion_list:
        continue

    attr_operator = getattr(operator, method)
    attr_type = type(getattr(operator, method))

    if "builtin_function_or_method" not in str(attr_type):
        continue
    try:
        type(getattr(series, method))
    except AttributeError:
        raise AttributeError(f"{method} | {attr_type}")

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

# print(
#     f"{len(methods)    = }",
#     f"{len(builtins)   = }",
#     f"{len(properties) = }",
#     sep = "\n"
# )

# %%
intro_text = [
    "\"\"\"Auto-generated dunder method col implementation\"\"\"",
    "",
    "# %% Imports",
    "from abc import abstractmethod",
    "from dataclasses import dataclass",
    "from typing import Any, Callable",
    "",
    "import numpy as np",
    "import numpy.typing as npt",
    "from pandas.core.internals.api import Dtype",
    "",
    "bool_t = bool",
    "",
    "# %% Classes and functions",
    "def is_col_test(obj):",
    "    return hasattr(obj, \"_is_col\")",
    "",
    "class BaseCol(object):",
    "    _is_col = True",
    "",
    "    @abstractmethod",
    "    def __call__(self, df):",
    "        pass",
    "",
]

# %% Write the code for properties
property_text = []

for property_name in properties:
    text = [
        f"    def {property_name}(self, DF):",
        f"        return self.__call__(DF).{property_name}",
        "",
    ]
    property_text += text

# %% Write the code for methods
method_text = []

methods_to_exclude = [
    "__init__",
    "__new__",
    "__copy__",
    "__deepcopy__",
    "__delattr__",
    "__delitem__",
    "__dir__",
    "__finalize__",
    "__getattr__",
    "__getattribute__",
    "__getitem__",
    "__getstate__",
    "__iter__",
    "__repr__",
    "__setattr__",
    "__setitem__",
    "__setstate__",
    "__sizeof__",
    "__str__",
]

for method in methods:
    if method in methods_to_exclude:
        continue

    attr = getattr(series, method)
    params = inspect.signature(attr).parameters

    param_names = params.keys()
    param_names_str = ", ".join(param_names).replace("'", "\"")

    param_names_with_self = ["self", *param_names]
    param_names_with_self_str = ", ".join(param_names).replace("'", "\"")

    params_with_default_args = [str(value) for value in params.values()]
    params_with_default_args_str = ", ".join(params_with_default_args).replace("'", "\"")

    params_with_self_with_default_args = ["self", *[str(value) for value in params.values()]]
    params_with_self_with_default_args_str = ", ".join(params_with_self_with_default_args).replace("'", "\"")


    if "other" in params:
        params_str_DF = param_names_str.replace("other", "other(DF)")

        text = [
            f"    def {method}({params_with_self_with_default_args_str}):",
            f"        if is_col_test(other):",
            f"            return CallCol(lambda DF: self.__call__(DF).{method}({params_str_DF}))",
            f"        else:",
            f"            return CallCol(lambda DF: self.__call__(DF).{method}({param_names_str}))",
            f"",
        ]
    else:
        text = [
            f"    def {method}({params_with_self_with_default_args_str}):",
            f"        return CallCol(lambda DF: self.__call__(DF).{method}({param_names_str}))",
            f"",
        ]

    method_text += text

# %% Write the code for builtins
checked_builtins = [
    '__format__',
    '__init_subclass__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__subclasshook__',
]

for builtin_name in builtins:
    if builtin_name not in checked_builtins:
        raise Exception("There's a builtin not accounted")

# %% Write the code for extra methods
extra_method_text = []

for method in extra_methods:
    if method != "__weakref__":
        params = inspect.signature(series.__class__).parameters

    param_names = ["self", *params.keys()]
    param_names_str = ", ".join(param_names).replace("'", "\"")

    params_with_default_args = ["self", *[str(value) for value in params.values()]]
    params_with_default_args_str = ", ".join(params_with_default_args).replace("'", "\"")

    if method == "__class__":
        params_str_DF = param_names_str.replace("data", "data(DF)")

        text = [
            f"    def {method}({params_with_default_args_str}):",
            f"        if is_col_test(data):",
            f"            return CallCol(lambda DF: self.__call__(DF).{method}({params_str_DF}))",
            f"        else:",
            f"            return CallCol(lambda DF: self.__call__(DF).{method}({param_names_str}))",
            f"",
        ]
    elif method == "__weakref__":
        text = [
            f"    def {method}(self):",
            f"        return CallCol(lambda DF: self.__call__(DF).{method}())",
            f"",
        ]
    else:
        raise Exception("{method} is in the list of extra_methods, but doesn't have a function builder")

    extra_method_text += text

final_text = [
    "@dataclass",
    "class Col(BaseCol):",
    "    col_name: Any",
    "    ",
    "    def __call__(self, DF):",
    "        return DF[self.col_name]",
    "",
    "@dataclass",
    "class CallCol(BaseCol):",
    "    fn: Callable",
    "    ",
    "    def __call__(self, DF):",
    "        return self.fn(DF)",
    "",
]

# %%
output = [
    *intro_text,
    *property_text,
    *method_text,
    *extra_method_text,
    *final_text,
]

# %%
with open("dunder_methods_autogen.py", "w") as f:
    f.write("\n".join(output))

# %%
