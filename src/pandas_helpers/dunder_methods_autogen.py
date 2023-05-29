"""Auto-generated dunder method col implementation"""
from __future__ import annotations

from collections.abc import Callable

# %% Imports
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any

import numpy as np
import numpy.typing as npt
from pandas.core.internals.api import Dtype

bool_t = bool

# %% Classes and functions
def is_col_test(obj):
    return hasattr(obj, "_is_col")

class BaseCol(object):
    _is_col = True

    @abstractmethod
    def __call__(self, df):
        pass

    def __annotations__(self, DF):
        return self.__call__(DF).__annotations__

    def __array_priority__(self, DF):
        return self.__call__(DF).__array_priority__

    def __dict__(self, DF):
        return self.__call__(DF).__dict__

    def __doc__(self, DF):
        return self.__call__(DF).__doc__

    def __hash__(self, DF):
        return self.__call__(DF).__hash__

    def __module__(self, DF):
        return self.__call__(DF).__module__

    def __abs__(self):
        return CallCol(lambda DF: self.__call__(DF).__abs__())

    def __add__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__add__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__add__(other))

    def __and__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__and__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__and__(other))

    def __array__(self, dtype: "npt.DTypeLike | None" = None):
        return CallCol(lambda DF: self.__call__(DF).__array__(dtype))

    def __array_ufunc__(self, ufunc: "np.ufunc", method: "str", *inputs: "Any", **kwargs: "Any"):
        return CallCol(lambda DF: self.__call__(DF).__array_ufunc__(ufunc, method, inputs, kwargs))

    def __bool__(self):
        return CallCol(lambda DF: self.__call__(DF).__bool__())

    def __contains__(self, key):
        return CallCol(lambda DF: self.__call__(DF).__contains__(key))

    def __divmod__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__divmod__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__divmod__(other))

    def __eq__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__eq__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__eq__(other))

    def __float__(self):
        return CallCol(lambda DF: self.__call__(DF).__float__())

    def __floordiv__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__floordiv__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__floordiv__(other))

    def __ge__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__ge__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__ge__(other))

    def __gt__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__gt__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__gt__(other))

    def __iadd__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__iadd__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__iadd__(other))

    def __iand__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__iand__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__iand__(other))

    def __ifloordiv__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__ifloordiv__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__ifloordiv__(other))

    def __imod__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__imod__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__imod__(other))

    def __imul__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__imul__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__imul__(other))

    def __int__(self):
        return CallCol(lambda DF: self.__call__(DF).__int__())

    def __invert__(self):
        return CallCol(lambda DF: self.__call__(DF).__invert__())

    def __ior__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__ior__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__ior__(other))

    def __ipow__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__ipow__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__ipow__(other))

    def __isub__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__isub__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__isub__(other))

    def __itruediv__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__itruediv__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__itruediv__(other))

    def __ixor__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__ixor__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__ixor__(other))

    def __le__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__le__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__le__(other))

    def __len__(self):
        return CallCol(lambda DF: self.__call__(DF).__len__())

    def __lt__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__lt__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__lt__(other))

    def __matmul__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__matmul__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__matmul__(other))

    def __mod__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__mod__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__mod__(other))

    def __mul__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__mul__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__mul__(other))

    def __ne__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__ne__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__ne__(other))

    def __neg__(self):
        return CallCol(lambda DF: self.__call__(DF).__neg__())

    def __nonzero__(self):
        return CallCol(lambda DF: self.__call__(DF).__nonzero__())

    def __or__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__or__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__or__(other))

    def __pos__(self):
        return CallCol(lambda DF: self.__call__(DF).__pos__())

    def __pow__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__pow__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__pow__(other))

    def __radd__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__radd__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__radd__(other))

    def __rand__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rand__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rand__(other))

    def __rdivmod__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rdivmod__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rdivmod__(other))

    def __rfloordiv__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rfloordiv__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rfloordiv__(other))

    def __rmatmul__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rmatmul__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rmatmul__(other))

    def __rmod__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rmod__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rmod__(other))

    def __rmul__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rmul__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rmul__(other))

    def __ror__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__ror__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__ror__(other))

    def __round__(self, decimals: "int" = 0):
        return CallCol(lambda DF: self.__call__(DF).__round__(decimals))

    def __rpow__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rpow__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rpow__(other))

    def __rsub__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rsub__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rsub__(other))

    def __rtruediv__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rtruediv__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rtruediv__(other))

    def __rxor__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__rxor__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__rxor__(other))

    def __sub__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__sub__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__sub__(other))

    def __truediv__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__truediv__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__truediv__(other))

    def __xor__(self, other):
        if is_col_test(other):
            return CallCol(lambda DF: self.__call__(DF).__xor__(other(DF)))
        else:
            return CallCol(lambda DF: self.__call__(DF).__xor__(other))

    def __class__(self, data=None, index=None, dtype: "Dtype | None" = None, name=None, copy: "bool | None" = None, fastpath: "bool" = False):
        if is_col_test(data):
            return CallCol(lambda DF: self.__call__(DF).__class__(self, data(DF), index, dtype, name, copy, fastpath))
        else:
            return CallCol(lambda DF: self.__call__(DF).__class__(self, data, index, dtype, name, copy, fastpath))

    def __weakref__(self):
        return CallCol(lambda DF: self.__call__(DF).__weakref__())

@dataclass
class Col(BaseCol):
    col_name: Any

    def __call__(self, DF):
        return DF[self.col_name]

@dataclass
class CallCol(BaseCol):
    fn: Callable

    def __call__(self, DF):
        return self.fn(DF)
