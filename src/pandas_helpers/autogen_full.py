"""Auto-generated dunder method col implementation"""

# %% Imports
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Literal, Hashable, IO, Optional, Union
import re

import numpy as np
import numpy.typing as npt

import pandas as pd
from pandas import Series, DataFrame
from pandas.core.indexers.objects import BaseIndexer
from pandas.core.arrays.base import ExtensionArray
from pandas.io.pytables import HDFStore
from pandas._libs.tslibs import BaseOffset
from pandas._typing import (
    AggFuncType,
    AlignJoin,
    AnyAll,
    AnyArrayLike,
    Axis,
    AxisInt,
    CompressionOptions,
    CorrelationMethod,
    DropKeep,
    Dtype,
    DtypeArg,
    DtypeBackend,
    FilePath,
    FillnaOptions,
    FloatFormatType,
    FormattersType,
    Frequency,
    IgnoreRaise,
    IndexKeyFunc,
    IndexLabel,
    IntervalClosedType,
    JSONSerializable,
    Level,
    Mapping,
    NaPosition,
    QuantileInterpolation,
    RandomState,
    Renamer,
    Scalar,
    Sequence,
    SortKind,
    StorageOptions,
    Suffixes,
    TimeAmbiguous,
    TimedeltaConvertibleTypes,
    TimeNonexistent,
    TimestampConvertibleTypes,
    ValueKeyFunc,
    WriteBuffer,
)
from pandas._libs import lib

ScalarLike_co = Union[
        int,
        float,
        complex,
        str,
        bytes,
        np.generic,
    ]
NumpySorter = Optional[np._typing._ArrayLikeInt_co]
NumpyValueArrayLike = Union[ScalarLike_co, npt.ArrayLike]

bool_t = bool

# %% Classes and functions
def is_col_test(obj):
    return hasattr(obj, "_is_col")

def decide_if_call(obj, DF):
    return obj(DF) if is_col_test(obj) else obj

class AtIndexer:
    def __init__(self, func):
        self.func = func
    def __getitem__(self, *indexes):
        return CallCol(lambda DF: self.func(DF).at.__getitem__(*indexes))

class IatIndexer:
    def __init__(self, func):
        self.func = func
    def __getitem__(self, *indexes):
        return CallCol(lambda DF: self.func(DF).iat.__getitem__(*indexes))

class IlocIndexer:
    def __init__(self, func):
        self.func = func
    def __getitem__(self, *indexes):
        return CallCol(lambda DF: self.func(DF).iloc.__getitem__(*indexes))

class LocIndexer:
    def __init__(self, func):
        self.func = func
    def __getitem__(self, *indexes):
        return CallCol(lambda DF: self.func(DF).loc.__getitem__(*indexes))

@dataclass
class StrAccessor(object):
    _fn: Callable

    def capitalize(self):
        return CallCol(lambda DF: self._fn(DF).str.capitalize())

    def casefold(self):
        return CallCol(lambda DF: self._fn(DF).str.casefold())

    def cat(self, others=None, sep=None, na_rep=None, join: 'AlignJoin' = 'left'):
        return CallCol(lambda DF: self._fn(DF).str.cat(decide_if_call(others, DF), sep, na_rep, join))

    def center(self, width, fillchar: 'str' = ' '):
        return CallCol(lambda DF: self._fn(DF).str.center(width, fillchar))

    def contains(self, pat, case: 'bool' = True, flags: 'int' = 0, na=None, regex: 'bool' = True):
        return CallCol(lambda DF: self._fn(DF).str.contains(pat, case, flags, na, regex))

    def count(self, pat, flags: 'int' = 0):
        return CallCol(lambda DF: self._fn(DF).str.count(pat, flags))

    def decode(self, encoding, errors: 'str' = 'strict'):
        return CallCol(lambda DF: self._fn(DF).str.decode(encoding, errors))

    def encode(self, encoding, errors: 'str' = 'strict'):
        return CallCol(lambda DF: self._fn(DF).str.encode(encoding, errors))

    def endswith(self, pat: 'str | tuple[str, ...]', na: 'Scalar | None' = None):
        return CallCol(lambda DF: self._fn(DF).str.endswith(pat, na))

    def extract(self, pat: 'str', flags: 'int' = 0, expand: 'bool' = True):
        return CallCol(lambda DF: self._fn(DF).str.extract(pat, flags, expand))

    def extractall(self, pat, flags: 'int' = 0):
        return CallCol(lambda DF: self._fn(DF).str.extractall(pat, flags))

    def find(self, sub, start: 'int' = 0, end=None):
        return CallCol(lambda DF: self._fn(DF).str.find(sub, start, end))

    def findall(self, pat, flags: 'int' = 0):
        return CallCol(lambda DF: self._fn(DF).str.findall(pat, flags))

    def fullmatch(self, pat, case: 'bool' = True, flags: 'int' = 0, na=None):
        return CallCol(lambda DF: self._fn(DF).str.fullmatch(pat, case, flags, na))

    def get(self, i):
        return CallCol(lambda DF: self._fn(DF).str.get(i))

    def get_dummies(self, sep: 'str' = '|'):
        return CallCol(lambda DF: self._fn(DF).str.get_dummies(sep))

    def index(self, sub, start: 'int' = 0, end=None):
        return CallCol(lambda DF: self._fn(DF).str.index(sub, start, end))

    def isalnum(self):
        return CallCol(lambda DF: self._fn(DF).str.isalnum())

    def isalpha(self):
        return CallCol(lambda DF: self._fn(DF).str.isalpha())

    def isdecimal(self):
        return CallCol(lambda DF: self._fn(DF).str.isdecimal())

    def isdigit(self):
        return CallCol(lambda DF: self._fn(DF).str.isdigit())

    def islower(self):
        return CallCol(lambda DF: self._fn(DF).str.islower())

    def isnumeric(self):
        return CallCol(lambda DF: self._fn(DF).str.isnumeric())

    def isspace(self):
        return CallCol(lambda DF: self._fn(DF).str.isspace())

    def istitle(self):
        return CallCol(lambda DF: self._fn(DF).str.istitle())

    def isupper(self):
        return CallCol(lambda DF: self._fn(DF).str.isupper())

    def join(self, sep):
        return CallCol(lambda DF: self._fn(DF).str.join(sep))

    def len(self):
        return CallCol(lambda DF: self._fn(DF).str.len())

    def ljust(self, width, fillchar: 'str' = ' '):
        return CallCol(lambda DF: self._fn(DF).str.ljust(width, fillchar))

    def lower(self):
        return CallCol(lambda DF: self._fn(DF).str.lower())

    def lstrip(self, to_strip=None):
        return CallCol(lambda DF: self._fn(DF).str.lstrip(to_strip))

    def match(self, pat, case: 'bool' = True, flags: 'int' = 0, na=None):
        return CallCol(lambda DF: self._fn(DF).str.match(pat, case, flags, na))

    def normalize(self, form):
        return CallCol(lambda DF: self._fn(DF).str.normalize(form))

    def pad(self, width, side: "Literal['left', 'right', 'both']" = 'left', fillchar: 'str' = ' '):
        return CallCol(lambda DF: self._fn(DF).str.pad(width, side, fillchar))

    def partition(self, sep: 'str' = ' ', expand: 'bool' = True):
        return CallCol(lambda DF: self._fn(DF).str.partition(sep, expand))

    def removeprefix(self, prefix):
        return CallCol(lambda DF: self._fn(DF).str.removeprefix(prefix))

    def removesuffix(self, suffix):
        return CallCol(lambda DF: self._fn(DF).str.removesuffix(suffix))

    def repeat(self, repeats):
        return CallCol(lambda DF: self._fn(DF).str.repeat(repeats))

    def replace(self, pat: 'str | re.Pattern', repl: 'str | Callable', n: 'int' = -1, case: 'bool | None' = None, flags: 'int' = 0, regex: 'bool' = False):
        return CallCol(lambda DF: self._fn(DF).str.replace(pat, repl, n, case, flags, regex))

    def rfind(self, sub, start: 'int' = 0, end=None):
        return CallCol(lambda DF: self._fn(DF).str.rfind(sub, start, end))

    def rindex(self, sub, start: 'int' = 0, end=None):
        return CallCol(lambda DF: self._fn(DF).str.rindex(sub, start, end))

    def rjust(self, width, fillchar: 'str' = ' '):
        return CallCol(lambda DF: self._fn(DF).str.rjust(width, fillchar))

    def rpartition(self, sep: 'str' = ' ', expand: 'bool' = True):
        return CallCol(lambda DF: self._fn(DF).str.rpartition(sep, expand))

    def rsplit(self, pat=None, n=-1, expand: 'bool' = False):
        return CallCol(lambda DF: self._fn(DF).str.rsplit(pat, n, expand))

    def rstrip(self, to_strip=None):
        return CallCol(lambda DF: self._fn(DF).str.rstrip(to_strip))

    def slice(self, start=None, stop=None, step=None):
        return CallCol(lambda DF: self._fn(DF).str.slice(start, stop, step))

    def slice_replace(self, start=None, stop=None, repl=None):
        return CallCol(lambda DF: self._fn(DF).str.slice_replace(start, stop, repl))

    def split(self, pat: 'str | re.Pattern | None' = None, n=-1, expand: 'bool' = False, regex: 'bool | None' = None):
        return CallCol(lambda DF: self._fn(DF).str.split(pat, n, expand, regex))

    def startswith(self, pat: 'str | tuple[str, ...]', na: 'Scalar | None' = None):
        return CallCol(lambda DF: self._fn(DF).str.startswith(pat, na))

    def strip(self, to_strip=None):
        return CallCol(lambda DF: self._fn(DF).str.strip(to_strip))

    def swapcase(self):
        return CallCol(lambda DF: self._fn(DF).str.swapcase())

    def title(self):
        return CallCol(lambda DF: self._fn(DF).str.title())

    def translate(self, table):
        return CallCol(lambda DF: self._fn(DF).str.translate(table))

    def upper(self):
        return CallCol(lambda DF: self._fn(DF).str.upper())

    def wrap(self, width, **kwargs):
        return CallCol(lambda DF: self._fn(DF).str.wrap(width, **kwargs))

    def zfill(self, width):
        return CallCol(lambda DF: self._fn(DF).str.zfill(width))

@dataclass
class CatAccessor(object):
    _fn: Callable

    @property
    def categories(self, DF):
        return self._fn(DF).cat.categories

    @property
    def codes(self, DF):
        return self._fn(DF).cat.codes

    @property
    def ordered(self, DF):
        return self._fn(DF).cat.ordered

    def add_categories(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.add_categories(*args, **kwargs))

    def as_ordered(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.as_ordered(*args, **kwargs))

    def as_unordered(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.as_unordered(*args, **kwargs))

    def remove_categories(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.remove_categories(*args, **kwargs))

    def remove_unused_categories(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.remove_unused_categories(*args, **kwargs))

    def rename_categories(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.rename_categories(*args, **kwargs))

    def reorder_categories(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.reorder_categories(*args, **kwargs))

    def set_categories(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).cat.set_categories(*args, **kwargs))

@dataclass
class DtAccessor(object):
    _fn: Callable

    @property
    def date(self, DF):
        return self._fn(DF).dt.date

    @property
    def day(self, DF):
        return self._fn(DF).dt.day

    @property
    def day_of_week(self, DF):
        return self._fn(DF).dt.day_of_week

    @property
    def day_of_year(self, DF):
        return self._fn(DF).dt.day_of_year

    @property
    def dayofweek(self, DF):
        return self._fn(DF).dt.dayofweek

    @property
    def dayofyear(self, DF):
        return self._fn(DF).dt.dayofyear

    @property
    def days_in_month(self, DF):
        return self._fn(DF).dt.days_in_month

    @property
    def daysinmonth(self, DF):
        return self._fn(DF).dt.daysinmonth

    @property
    def freq(self, DF):
        return self._fn(DF).dt.freq

    @property
    def hour(self, DF):
        return self._fn(DF).dt.hour

    @property
    def is_leap_year(self, DF):
        return self._fn(DF).dt.is_leap_year

    @property
    def is_month_end(self, DF):
        return self._fn(DF).dt.is_month_end

    @property
    def is_month_start(self, DF):
        return self._fn(DF).dt.is_month_start

    @property
    def is_quarter_end(self, DF):
        return self._fn(DF).dt.is_quarter_end

    @property
    def is_quarter_start(self, DF):
        return self._fn(DF).dt.is_quarter_start

    @property
    def is_year_end(self, DF):
        return self._fn(DF).dt.is_year_end

    @property
    def is_year_start(self, DF):
        return self._fn(DF).dt.is_year_start

    @property
    def microsecond(self, DF):
        return self._fn(DF).dt.microsecond

    @property
    def minute(self, DF):
        return self._fn(DF).dt.minute

    @property
    def month(self, DF):
        return self._fn(DF).dt.month

    @property
    def nanosecond(self, DF):
        return self._fn(DF).dt.nanosecond

    @property
    def quarter(self, DF):
        return self._fn(DF).dt.quarter

    @property
    def second(self, DF):
        return self._fn(DF).dt.second

    @property
    def time(self, DF):
        return self._fn(DF).dt.time

    @property
    def timetz(self, DF):
        return self._fn(DF).dt.timetz

    @property
    def tz(self, DF):
        return self._fn(DF).dt.tz

    @property
    def unit(self, DF):
        return self._fn(DF).dt.unit

    @property
    def weekday(self, DF):
        return self._fn(DF).dt.weekday

    @property
    def year(self, DF):
        return self._fn(DF).dt.year

    def as_unit(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.as_unit(*args, **kwargs))

    def ceil(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.ceil(*args, **kwargs))

    def day_name(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.day_name(*args, **kwargs))

    def floor(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.floor(*args, **kwargs))

    def isocalendar(self):
        return CallCol(lambda DF: self._fn(DF).dt.isocalendar())

    def month_name(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.month_name(*args, **kwargs))

    def normalize(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.normalize(*args, **kwargs))

    def round(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.round(*args, **kwargs))

    def strftime(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.strftime(*args, **kwargs))

    def to_period(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.to_period(*args, **kwargs))

    def to_pydatetime(self):
        return CallCol(lambda DF: self._fn(DF).dt.to_pydatetime())

    def tz_convert(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.tz_convert(*args, **kwargs))

    def tz_localize(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).dt.tz_localize(*args, **kwargs))

@dataclass
class SparseAccessor(object):
    _fn: Callable

    @property
    def density(self, DF):
        return self._fn(DF).sparse.density

    @property
    def fill_value(self, DF):
        return self._fn(DF).sparse.fill_value

    @property
    def npoints(self, DF):
        return self._fn(DF).sparse.npoints

    @property
    def sp_values(self, DF):
        return self._fn(DF).sparse.sp_values

    def from_coo(self, A, dense_index: 'bool' = False):
        return CallCol(lambda DF: self._fn(DF).sparse.from_coo(A, dense_index))

    def to_coo(self, row_levels=(0,), column_levels=(1,), sort_labels: 'bool' = False):
        return CallCol(lambda DF: self._fn(DF).sparse.to_coo(row_levels, column_levels, sort_labels))

    def to_dense(self):
        return CallCol(lambda DF: self._fn(DF).sparse.to_dense())

@dataclass
class PlotAccessor(object):
    _fn: Callable

    def area(self, x=None, y=None, stacked: 'bool' = True, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.area(x, y, stacked, **kwargs))

    def bar(self, x=None, y=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.bar(x, y, **kwargs))

    def barh(self, x=None, y=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.barh(x, y, **kwargs))

    def box(self, by=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.box(by, **kwargs))

    def density(self, bw_method=None, ind=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.density(bw_method, ind, **kwargs))

    def hexbin(self, x, y, C=None, reduce_C_function=None, gridsize=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.hexbin(x, y, C, reduce_C_function, gridsize, **kwargs))

    def hist(self, by=None, bins: 'int' = 10, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.hist(by, bins, **kwargs))

    def kde(self, bw_method=None, ind=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.kde(bw_method, ind, **kwargs))

    def line(self, x=None, y=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.line(x, y, **kwargs))

    def pie(self, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.pie(**kwargs))

    def scatter(self, x, y, s=None, c=None, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.scatter(x, y, s, c, **kwargs))

    def __call__(self, *args, **kwargs):
        return CallCol(lambda DF: self._fn(DF).plot.__call__(*args, **kwargs))

class BaseCol(object):
    _is_col = True

    @abstractmethod
    def __call__(self, df):
        pass

    def __getitem__(self, *indexes):
        return CallCol(lambda DF: self.__call__(DF).at.__getitem__(*indexes))

    @property
    def __annotations__(self, DF):
        return self.__call__(DF).__annotations__

    @property
    def __array_priority__(self, DF):
        return self.__call__(DF).__array_priority__

    @property
    def __dict__(self, DF):
        return self.__call__(DF).__dict__

    @property
    def __doc__(self, DF):
        return self.__call__(DF).__doc__

    @property
    def __hash__(self, DF):
        return self.__call__(DF).__hash__

    @property
    def __module__(self, DF):
        return self.__call__(DF).__module__

    @property
    def cat(self):
        return CatAccessor(self.__call__)

    @property
    def dt(self):
        return DtAccessor(self.__call__)

    @property
    def str(self):
        return StrAccessor(self.__call__)

    @property
    def sparse(self):
        return SparseAccessor(self.__call__)

    @property
    def plot(self):
        return PlotAccessor(self.__call__)

    @property
    def T(self, DF):
        return self.__call__(DF).T

    @property
    def array(self, DF):
        return self.__call__(DF).array

    @property
    def attrs(self, DF):
        return self.__call__(DF).attrs

    @property
    def axes(self, DF):
        return self.__call__(DF).axes

    @property
    def dtype(self, DF):
        return self.__call__(DF).dtype

    @property
    def dtypes(self, DF):
        return self.__call__(DF).dtypes

    @property
    def empty(self, DF):
        return self.__call__(DF).empty

    @property
    def flags(self, DF):
        return self.__call__(DF).flags

    @property
    def hasnans(self, DF):
        return self.__call__(DF).hasnans

    @property
    def index(self, DF):
        return self.__call__(DF).index

    @property
    def is_monotonic_decreasing(self, DF):
        return self.__call__(DF).is_monotonic_decreasing

    @property
    def is_monotonic_increasing(self, DF):
        return self.__call__(DF).is_monotonic_increasing

    @property
    def is_unique(self, DF):
        return self.__call__(DF).is_unique

    @property
    def name(self, DF):
        return self.__call__(DF).name

    @property
    def nbytes(self, DF):
        return self.__call__(DF).nbytes

    @property
    def ndim(self, DF):
        return self.__call__(DF).ndim

    @property
    def shape(self, DF):
        return self.__call__(DF).shape

    @property
    def size(self, DF):
        return self.__call__(DF).size

    @property
    def values(self, DF):
        return self.__call__(DF).values

    @property
    def at(self):
        return AtIndexer(self.__call__)

    @property
    def iat(self):
        return IatIndexer(self.__call__)

    @property
    def iloc(self):
        return IlocIndexer(self.__call__)

    @property
    def loc(self):
        return LocIndexer(self.__call__)

    def __abs__(self):
        return CallCol(lambda DF: self.__call__(DF).__abs__())

    def __add__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__add__(decide_if_call(other, DF)))

    def __and__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__and__(decide_if_call(other, DF)))

    def __array__(self, dtype: 'npt.DTypeLike | None' = None):
        return CallCol(lambda DF: self.__call__(DF).__array__(dtype))

    def __array_ufunc__(self, ufunc: 'np.ufunc', method: 'str', *inputs: 'Any', **kwargs: 'Any'):
        return CallCol(lambda DF: self.__call__(DF).__array_ufunc__(ufunc, method, inputs, **kwargs))

    def __bool__(self):
        return CallCol(lambda DF: self.__call__(DF).__bool__())

    def __class__(self, data=None, index=None, dtype: 'Dtype | None' = None, name=None, copy: 'bool | None' = None, fastpath: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).__class__(decide_if_call(data, DF), index, dtype, name, copy, fastpath))

    def __contains__(self, key):
        return CallCol(lambda DF: self.__call__(DF).__contains__(key))

    def __divmod__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__divmod__(decide_if_call(other, DF)))

    def __eq__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__eq__(decide_if_call(other, DF)))

    def __float__(self):
        return CallCol(lambda DF: self.__call__(DF).__float__())

    def __floordiv__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__floordiv__(decide_if_call(other, DF)))

    def __ge__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__ge__(decide_if_call(other, DF)))

    def __gt__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__gt__(decide_if_call(other, DF)))

    def __iadd__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__iadd__(decide_if_call(other, DF)))

    def __iand__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__iand__(decide_if_call(other, DF)))

    def __ifloordiv__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__ifloordiv__(decide_if_call(other, DF)))

    def __imod__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__imod__(decide_if_call(other, DF)))

    def __imul__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__imul__(decide_if_call(other, DF)))

    def __int__(self):
        return CallCol(lambda DF: self.__call__(DF).__int__())

    def __invert__(self):
        return CallCol(lambda DF: self.__call__(DF).__invert__())

    def __ior__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__ior__(decide_if_call(other, DF)))

    def __ipow__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__ipow__(decide_if_call(other, DF)))

    def __isub__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__isub__(decide_if_call(other, DF)))

    def __itruediv__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__itruediv__(decide_if_call(other, DF)))

    def __ixor__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__ixor__(decide_if_call(other, DF)))

    def __le__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__le__(decide_if_call(other, DF)))

    def __len__(self):
        return CallCol(lambda DF: self.__call__(DF).__len__())

    def __lt__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__lt__(decide_if_call(other, DF)))

    def __matmul__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__matmul__(decide_if_call(other, DF)))

    def __mod__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__mod__(decide_if_call(other, DF)))

    def __mul__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__mul__(decide_if_call(other, DF)))

    def __ne__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__ne__(decide_if_call(other, DF)))

    def __neg__(self):
        return CallCol(lambda DF: self.__call__(DF).__neg__())

    def __nonzero__(self):
        return CallCol(lambda DF: self.__call__(DF).__nonzero__())

    def __or__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__or__(decide_if_call(other, DF)))

    def __pos__(self):
        return CallCol(lambda DF: self.__call__(DF).__pos__())

    def __pow__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__pow__(decide_if_call(other, DF)))

    def __radd__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__radd__(decide_if_call(other, DF)))

    def __rand__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rand__(decide_if_call(other, DF)))

    def __rdivmod__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rdivmod__(decide_if_call(other, DF)))

    def __rfloordiv__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rfloordiv__(decide_if_call(other, DF)))

    def __rmatmul__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rmatmul__(decide_if_call(other, DF)))

    def __rmod__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rmod__(decide_if_call(other, DF)))

    def __rmul__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rmul__(decide_if_call(other, DF)))

    def __ror__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__ror__(decide_if_call(other, DF)))

    def __round__(self, decimals: 'int' = 0):
        return CallCol(lambda DF: self.__call__(DF).__round__(decimals))

    def __rpow__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rpow__(decide_if_call(other, DF)))

    def __rsub__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rsub__(decide_if_call(other, DF)))

    def __rtruediv__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rtruediv__(decide_if_call(other, DF)))

    def __rxor__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__rxor__(decide_if_call(other, DF)))

    def __sub__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__sub__(decide_if_call(other, DF)))

    def __truediv__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__truediv__(decide_if_call(other, DF)))

    def __xor__(self, other):
        return CallCol(lambda DF: self.__call__(DF).__xor__(decide_if_call(other, DF)))

    def abs(self):
        return CallCol(lambda DF: self.__call__(DF).abs())

    def add(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).add(decide_if_call(other, DF), level, fill_value, axis))

    def add_prefix(self, prefix: 'str', axis: 'Axis | None' = None):
        return CallCol(lambda DF: self.__call__(DF).add_prefix(prefix, axis))

    def add_suffix(self, suffix: 'str', axis: 'Axis | None' = None):
        return CallCol(lambda DF: self.__call__(DF).add_suffix(suffix, axis))

    def agg(self, func=None, axis: 'Axis' = 0, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).agg(func, axis, *args, **kwargs))

    def aggregate(self, func=None, axis: 'Axis' = 0, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).aggregate(func, axis, *args, **kwargs))

    def align(self, other: 'Series', join: 'AlignJoin' = 'outer', axis: 'Axis | None' = None, level: 'Level' = None, copy: 'bool | None' = None, fill_value: 'Hashable' = None, method: 'FillnaOptions | None' = None, limit: 'int | None' = None, fill_axis: 'Axis' = 0, broadcast_axis: 'Axis | None' = None):
        return CallCol(lambda DF: self.__call__(DF).align(decide_if_call(other, DF), join, axis, level, copy, fill_value, method, limit, fill_axis, broadcast_axis))

    def all(self, axis: 'Axis' = 0, bool_only=None, skipna: 'bool_t' = True, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).all(axis, bool_only, skipna, **kwargs))

    def any(self, axis: 'Axis' = 0, bool_only=None, skipna: 'bool_t' = True, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).any(axis, bool_only, skipna, **kwargs))

    def apply(self, func: 'AggFuncType', convert_dtype: 'bool' = True, args: 'tuple[Any, ...]' = (), **kwargs):
        return CallCol(lambda DF: self.__call__(DF).apply(func, convert_dtype, *args, **kwargs))

    def argmax(self, axis: 'AxisInt | None' = None, skipna: 'bool' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).argmax(axis, skipna, *args, **kwargs))

    def argmin(self, axis: 'AxisInt | None' = None, skipna: 'bool' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).argmin(axis, skipna, *args, **kwargs))

    def argsort(self, axis: 'Axis' = 0, kind: 'SortKind' = 'quicksort', order: 'None' = None):
        return CallCol(lambda DF: self.__call__(DF).argsort(axis, kind, order))

    def asfreq(self, freq: 'Frequency', method: 'FillnaOptions | None' = None, how: 'str | None' = None, normalize: 'bool' = False, fill_value: 'Hashable' = None):
        return CallCol(lambda DF: self.__call__(DF).asfreq(freq, method, how, normalize, fill_value))

    def asof(self, where, subset=None):
        return CallCol(lambda DF: self.__call__(DF).asof(where, subset))

    def astype(self, dtype, copy: 'bool_t | None' = None, errors: 'IgnoreRaise' = 'raise'):
        return CallCol(lambda DF: self.__call__(DF).astype(dtype, copy, errors))

    def at_time(self, time, asof: 'bool_t' = False, axis: 'Axis | None' = None):
        return CallCol(lambda DF: self.__call__(DF).at_time(time, asof, axis))

    def autocorr(self, lag: 'int' = 1):
        return CallCol(lambda DF: self.__call__(DF).autocorr(lag))

    def backfill(self, axis: 'None | Axis' = None, inplace: 'bool_t' = False, limit: 'None | int' = None, downcast: 'dict | None' = None):
        return CallCol(lambda DF: self.__call__(DF).backfill(axis, inplace, limit, downcast))

    def between(self, left, right, inclusive: "Literal['both', 'neither', 'left', 'right']" = 'both'):
        return CallCol(lambda DF: self.__call__(DF).between(left, right, inclusive))

    def between_time(self, start_time, end_time, inclusive: 'IntervalClosedType' = 'both', axis: 'Axis | None' = None):
        return CallCol(lambda DF: self.__call__(DF).between_time(start_time, end_time, inclusive, axis))

    def bfill(self, axis: 'None | Axis' = None, inplace: 'bool' = False, limit: 'None | int' = None, downcast: 'dict | None' = None):
        return CallCol(lambda DF: self.__call__(DF).bfill(axis, inplace, limit, downcast))

    def bool(self):
        return CallCol(lambda DF: self.__call__(DF).bool())

    def clip(self, lower=None, upper=None, axis: 'Axis | None' = None, inplace: 'bool' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).clip(lower, upper, axis, inplace, **kwargs))

    def combine(self, other: 'Series | Hashable', func: 'Callable[[Hashable, Hashable], Hashable]', fill_value: 'Hashable' = None):
        return CallCol(lambda DF: self.__call__(DF).combine(decide_if_call(other, DF), func, fill_value))

    def combine_first(self, other):
        return CallCol(lambda DF: self.__call__(DF).combine_first(decide_if_call(other, DF)))

    def compare(self, other: 'Series', align_axis: 'Axis' = 1, keep_shape: 'bool' = False, keep_equal: 'bool' = False, result_names: 'Suffixes' = ('self', 'other')):
        return CallCol(lambda DF: self.__call__(DF).compare(decide_if_call(other, DF), align_axis, keep_shape, keep_equal, result_names))

    def convert_dtypes(self, infer_objects: 'bool_t' = True, convert_string: 'bool_t' = True, convert_integer: 'bool_t' = True, convert_boolean: 'bool_t' = True, convert_floating: 'bool_t' = True, dtype_backend: 'DtypeBackend' = 'numpy_nullable'):
        return CallCol(lambda DF: self.__call__(DF).convert_dtypes(infer_objects, convert_string, convert_integer, convert_boolean, convert_floating, dtype_backend))

    def copy(self, deep: 'bool_t | None' = True):
        return CallCol(lambda DF: self.__call__(DF).copy(deep))

    def corr(self, other: 'Series', method: 'CorrelationMethod' = 'pearson', min_periods: 'int | None' = None):
        return CallCol(lambda DF: self.__call__(DF).corr(decide_if_call(other, DF), method, min_periods))

    def count(self):
        return CallCol(lambda DF: self.__call__(DF).count())

    def cov(self, other: 'Series', min_periods: 'int | None' = None, ddof: 'int | None' = 1):
        return CallCol(lambda DF: self.__call__(DF).cov(decide_if_call(other, DF), min_periods, ddof))

    def cummax(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).cummax(axis, skipna, *args, **kwargs))

    def cummin(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).cummin(axis, skipna, *args, **kwargs))

    def cumprod(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).cumprod(axis, skipna, *args, **kwargs))

    def cumsum(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).cumsum(axis, skipna, *args, **kwargs))

    def describe(self, percentiles=None, include=None, exclude=None):
        return CallCol(lambda DF: self.__call__(DF).describe(percentiles, include, exclude))

    def diff(self, periods: 'int' = 1):
        return CallCol(lambda DF: self.__call__(DF).diff(periods))

    def div(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).div(decide_if_call(other, DF), level, fill_value, axis))

    def divide(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).divide(decide_if_call(other, DF), level, fill_value, axis))

    def divmod(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).divmod(decide_if_call(other, DF), level, fill_value, axis))

    def dot(self, other: 'AnyArrayLike'):
        return CallCol(lambda DF: self.__call__(DF).dot(decide_if_call(other, DF)))

    def drop(self, labels: 'IndexLabel' = None, axis: 'Axis' = 0, index: 'IndexLabel' = None, columns: 'IndexLabel' = None, level: 'Level | None' = None, inplace: 'bool' = False, errors: 'IgnoreRaise' = 'raise'):
        return CallCol(lambda DF: self.__call__(DF).drop(labels, axis, index, columns, level, inplace, errors))

    def drop_duplicates(self, keep: 'DropKeep' = 'first', inplace: 'bool' = False, ignore_index: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).drop_duplicates(keep, inplace, ignore_index))

    def droplevel(self, level: 'IndexLabel', axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).droplevel(level, axis))

    def dropna(self, axis: 'Axis' = 0, inplace: 'bool' = False, how: 'AnyAll | None' = None, ignore_index: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).dropna(axis, inplace, how, ignore_index))

    def duplicated(self, keep: 'DropKeep' = 'first'):
        return CallCol(lambda DF: self.__call__(DF).duplicated(keep))

    def eq(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).eq(decide_if_call(other, DF), level, fill_value, axis))

    def equals(self, other: 'object'):
        return CallCol(lambda DF: self.__call__(DF).equals(decide_if_call(other, DF)))

    def ewm(self, com: 'float | None' = None, span: 'float | None' = None, halflife: 'float | TimedeltaConvertibleTypes | None' = None, alpha: 'float | None' = None, min_periods: 'int | None' = 0, adjust: 'bool_t' = True, ignore_na: 'bool_t' = False, axis: 'Axis' = 0, times: 'np.ndarray | DataFrame | Series | None' = None, method: 'str' = 'single'):
        return CallCol(lambda DF: self.__call__(DF).ewm(com, span, halflife, alpha, min_periods, adjust, ignore_na, axis, decide_if_call(times, DF), method))

    def expanding(self, min_periods: 'int' = 1, axis: 'Axis' = 0, method: 'str' = 'single'):
        return CallCol(lambda DF: self.__call__(DF).expanding(min_periods, axis, method))

    def explode(self, ignore_index: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).explode(ignore_index))

    def factorize(self, sort: 'bool' = False, use_na_sentinel: 'bool' = True):
        return CallCol(lambda DF: self.__call__(DF).factorize(sort, use_na_sentinel))

    def ffill(self, axis: 'None | Axis' = None, inplace: 'bool' = False, limit: 'None | int' = None, downcast: 'dict | None' = None):
        return CallCol(lambda DF: self.__call__(DF).ffill(axis, inplace, limit, downcast))

    def fillna(self, value: 'Hashable | Mapping | Series | DataFrame' = None, method: 'FillnaOptions | None' = None, axis: 'Axis | None' = None, inplace: 'bool' = False, limit: 'int | None' = None, downcast: 'dict | None' = None):
        return CallCol(lambda DF: self.__call__(DF).fillna(decide_if_call(value, DF), method, axis, inplace, limit, downcast))

    def filter(self, items=None, like: 'str | None' = None, regex: 'str | None' = None, axis: 'Axis | None' = None):
        return CallCol(lambda DF: self.__call__(DF).filter(items, like, regex, axis))

    def first(self, offset):
        return CallCol(lambda DF: self.__call__(DF).first(offset))

    def first_valid_index(self):
        return CallCol(lambda DF: self.__call__(DF).first_valid_index())

    def floordiv(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).floordiv(decide_if_call(other, DF), level, fill_value, axis))

    def ge(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).ge(decide_if_call(other, DF), level, fill_value, axis))

    def get(self, key, default=None):
        return CallCol(lambda DF: self.__call__(DF).get(key, default))

    def groupby(self, by=None, axis: 'Axis' = 0, level: 'IndexLabel' = None, as_index: 'bool' = True, sort: 'bool' = True, group_keys: 'bool' = True, observed: 'bool' = False, dropna: 'bool' = True):
        return CallCol(lambda DF: self.__call__(DF).groupby(by, axis, level, as_index, sort, group_keys, observed, dropna))

    def gt(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).gt(decide_if_call(other, DF), level, fill_value, axis))

    def head(self, n: 'int' = 5):
        return CallCol(lambda DF: self.__call__(DF).head(n))

    def hist(self, by=None, ax=None, grid: 'bool' = True, xlabelsize: 'int | None' = None, xrot: 'float | None' = None, ylabelsize: 'int | None' = None, yrot: 'float | None' = None, figsize: 'tuple[int, int] | None' = None, bins: 'int | Sequence[int]' = 10, backend: 'str | None' = None, legend: 'bool' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).hist(by, ax, grid, xlabelsize, xrot, ylabelsize, yrot, figsize, bins, backend, legend, **kwargs))

    def idxmax(self, axis: 'Axis' = 0, skipna: 'bool' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).idxmax(axis, skipna, *args, **kwargs))

    def idxmin(self, axis: 'Axis' = 0, skipna: 'bool' = True, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).idxmin(axis, skipna, *args, **kwargs))

    def infer_objects(self, copy: 'bool_t | None' = None):
        return CallCol(lambda DF: self.__call__(DF).infer_objects(copy))

    def info(self, verbose: 'bool | None' = None, buf: 'IO[str] | None' = None, max_cols: 'int | None' = None, memory_usage: 'bool | str | None' = None, show_counts: 'bool' = True):
        return CallCol(lambda DF: self.__call__(DF).info(verbose, buf, max_cols, memory_usage, show_counts))

    def interpolate(self, method: 'str' = 'linear', axis: 'Axis' = 0, limit: 'int | None' = None, inplace: 'bool' = False, limit_direction: 'str | None' = None, limit_area: 'str | None' = None, downcast: 'str | None' = None, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).interpolate(method, axis, limit, inplace, limit_direction, limit_area, downcast, **kwargs))

    def isin(self, values):
        return CallCol(lambda DF: self.__call__(DF).isin(values))

    def isna(self):
        return CallCol(lambda DF: self.__call__(DF).isna())

    def isnull(self):
        return CallCol(lambda DF: self.__call__(DF).isnull())

    def item(self):
        return CallCol(lambda DF: self.__call__(DF).item())

    def items(self):
        return CallCol(lambda DF: self.__call__(DF).items())

    def keys(self):
        return CallCol(lambda DF: self.__call__(DF).keys())

    def kurt(self, axis: 'Axis | None' = 0, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).kurt(axis, skipna, numeric_only, **kwargs))

    def kurtosis(self, axis: 'Axis | None' = 0, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).kurtosis(axis, skipna, numeric_only, **kwargs))

    def last(self, offset):
        return CallCol(lambda DF: self.__call__(DF).last(offset))

    def last_valid_index(self):
        return CallCol(lambda DF: self.__call__(DF).last_valid_index())

    def le(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).le(decide_if_call(other, DF), level, fill_value, axis))

    def lt(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).lt(decide_if_call(other, DF), level, fill_value, axis))

    def map(self, arg: 'Callable | Mapping | Series', na_action: "Literal['ignore'] | None" = None):
        return CallCol(lambda DF: self.__call__(DF).map(decide_if_call(arg, DF), na_action))

    def mask(self, cond, other=lib.no_default):
        return CallCol(lambda DF: self.__call__(DF).mask(decide_if_call(cond, DF), decide_if_call(other, DF)))

    def max(self, axis: 'AxisInt | None' = 0, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).max(axis, skipna, numeric_only, **kwargs))

    def mean(self, axis: 'AxisInt | None' = 0, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).mean(axis, skipna, numeric_only, **kwargs))

    def median(self, axis: 'AxisInt | None' = 0, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).median(axis, skipna, numeric_only, **kwargs))

    def memory_usage(self, index: 'bool' = True, deep: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).memory_usage(index, deep))

    def min(self, axis: 'AxisInt | None' = 0, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).min(axis, skipna, numeric_only, **kwargs))

    def mod(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).mod(decide_if_call(other, DF), level, fill_value, axis))

    def mode(self, dropna: 'bool' = True):
        return CallCol(lambda DF: self.__call__(DF).mode(dropna))

    def mul(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).mul(decide_if_call(other, DF), level, fill_value, axis))

    def multiply(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).multiply(decide_if_call(other, DF), level, fill_value, axis))

    def ne(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).ne(decide_if_call(other, DF), level, fill_value, axis))

    def nlargest(self, n: 'int' = 5, keep: "Literal['first', 'last', 'all']" = 'first'):
        return CallCol(lambda DF: self.__call__(DF).nlargest(n, keep))

    def notna(self):
        return CallCol(lambda DF: self.__call__(DF).notna())

    def notnull(self):
        return CallCol(lambda DF: self.__call__(DF).notnull())

    def nsmallest(self, n: 'int' = 5, keep: 'str' = 'first'):
        return CallCol(lambda DF: self.__call__(DF).nsmallest(n, keep))

    def nunique(self, dropna: 'bool' = True):
        return CallCol(lambda DF: self.__call__(DF).nunique(dropna))

    def pad(self, axis: 'None | Axis' = None, inplace: 'bool_t' = False, limit: 'None | int' = None, downcast: 'dict | None' = None):
        return CallCol(lambda DF: self.__call__(DF).pad(axis, inplace, limit, downcast))

    def pct_change(self, periods: 'int' = 1, fill_method: "Literal['backfill', 'bfill', 'pad', 'ffill'] | None" = 'pad', limit=None, freq=None, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).pct_change(periods, fill_method, limit, freq, **kwargs))

    def pipe(self, func: 'Callable[..., T] | tuple[Callable[..., T], str]', *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).pipe(func, *args, **kwargs))

    def pop(self, item: 'Hashable'):
        return CallCol(lambda DF: self.__call__(DF).pop(item))

    def pow(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).pow(decide_if_call(other, DF), level, fill_value, axis))

    def prod(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, min_count: 'int' = 0, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).prod(axis, skipna, numeric_only, min_count, **kwargs))

    def product(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, min_count: 'int' = 0, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).product(axis, skipna, numeric_only, min_count, **kwargs))

    def quantile(self, q: 'float | Sequence[float] | AnyArrayLike' = 0.5, interpolation: 'QuantileInterpolation' = 'linear'):
        return CallCol(lambda DF: self.__call__(DF).quantile(q, interpolation))

    def radd(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).radd(decide_if_call(other, DF), level, fill_value, axis))

    def rank(self, axis: 'Axis' = 0, method: 'str' = 'average', numeric_only: 'bool_t' = False, na_option: 'str' = 'keep', ascending: 'bool_t' = True, pct: 'bool_t' = False):
        return CallCol(lambda DF: self.__call__(DF).rank(axis, method, numeric_only, na_option, ascending, pct))

    def ravel(self, order: 'str' = 'C'):
        return CallCol(lambda DF: self.__call__(DF).ravel(order))

    def rdiv(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rdiv(decide_if_call(other, DF), level, fill_value, axis))

    def rdivmod(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rdivmod(decide_if_call(other, DF), level, fill_value, axis))

    def reindex(self, index=None, axis: 'Axis | None' = None, method: 'str | None' = None, copy: 'bool | None' = None, level: 'Level | None' = None, fill_value: 'Scalar | None' = None, limit: 'int | None' = None, tolerance=None):
        return CallCol(lambda DF: self.__call__(DF).reindex(index, axis, method, copy, level, fill_value, limit, tolerance))

    def reindex_like(self, other, method: "Literal['backfill', 'bfill', 'pad', 'ffill', 'nearest'] | None" = None, copy: 'bool_t | None' = None, limit=None, tolerance=None):
        return CallCol(lambda DF: self.__call__(DF).reindex_like(decide_if_call(other, DF), method, copy, limit, tolerance))

    def rename(self, index: 'Renamer | Hashable | None' = None, axis: 'Axis | None' = None, copy: 'bool' = True, inplace: 'bool' = False, level: 'Level | None' = None, errors: 'IgnoreRaise' = 'ignore'):
        return CallCol(lambda DF: self.__call__(DF).rename(index, axis, copy, inplace, level, errors))

    def rename_axis(self, mapper: 'IndexLabel | lib.NoDefault' = lib.no_default, index=lib.no_default, axis: 'Axis' = 0, copy: 'bool' = True, inplace: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).rename_axis(mapper, index, axis, copy, inplace))

    def reorder_levels(self, order: 'Sequence[Level]'):
        return CallCol(lambda DF: self.__call__(DF).reorder_levels(order))

    def repeat(self, repeats: 'int | Sequence[int]', axis: 'None' = None):
        return CallCol(lambda DF: self.__call__(DF).repeat(repeats, axis))

    def replace(self, to_replace=None, value=lib.no_default, inplace: 'bool' = False, limit: 'int | None' = None, regex: 'bool' = False, method: "Literal['pad', 'ffill', 'bfill'] | lib.NoDefault" = lib.no_default):
        return CallCol(lambda DF: self.__call__(DF).replace(to_replace, value, inplace, limit, regex, method))

    def resample(self, rule, axis: 'Axis' = 0, closed: 'str | None' = None, label: 'str | None' = None, convention: 'str' = 'start', kind: 'str | None' = None, on: 'Level' = None, level: 'Level' = None, origin: 'str | TimestampConvertibleTypes' = 'start_day', offset: 'TimedeltaConvertibleTypes | None' = None, group_keys: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).resample(rule, axis, closed, label, convention, kind, on, level, origin, offset, group_keys))

    def reset_index(self, level: 'IndexLabel' = None, drop: 'bool' = False, name: 'Level' = lib.no_default, inplace: 'bool' = False, allow_duplicates: 'bool' = False):
        return CallCol(lambda DF: self.__call__(DF).reset_index(level, drop, name, inplace, allow_duplicates))

    def rfloordiv(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rfloordiv(decide_if_call(other, DF), level, fill_value, axis))

    def rmod(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rmod(decide_if_call(other, DF), level, fill_value, axis))

    def rmul(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rmul(decide_if_call(other, DF), level, fill_value, axis))

    def rolling(self, window: 'int | dt.timedelta | str | BaseOffset | BaseIndexer', min_periods: 'int | None' = None, center: 'bool_t' = False, win_type: 'str | None' = None, on: 'str | None' = None, axis: 'Axis' = 0, closed: 'str | None' = None, step: 'int | None' = None, method: 'str' = 'single'):
        return CallCol(lambda DF: self.__call__(DF).rolling(window, min_periods, center, win_type, on, axis, closed, step, method))

    def round(self, decimals: 'int' = 0, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).round(decimals, *args, **kwargs))

    def rpow(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rpow(decide_if_call(other, DF), level, fill_value, axis))

    def rsub(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rsub(decide_if_call(other, DF), level, fill_value, axis))

    def rtruediv(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).rtruediv(decide_if_call(other, DF), level, fill_value, axis))

    def sample(self, n: 'int | None' = None, frac: 'float | None' = None, replace: 'bool_t' = False, weights=None, random_state: 'RandomState | None' = None, axis: 'Axis | None' = None, ignore_index: 'bool_t' = False):
        return CallCol(lambda DF: self.__call__(DF).sample(n, frac, replace, weights, random_state, axis, ignore_index))

    def searchsorted(self, value: 'NumpyValueArrayLike | ExtensionArray', side: "Literal['left', 'right']" = 'left', sorter: 'NumpySorter' = None):
        return CallCol(lambda DF: self.__call__(DF).searchsorted(value, side, sorter))

    def sem(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, ddof: 'int' = 1, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).sem(axis, skipna, ddof, numeric_only, **kwargs))

    def set_axis(self, labels, axis: 'Axis' = 0, copy: 'bool | None' = None):
        return CallCol(lambda DF: self.__call__(DF).set_axis(labels, axis, copy))

    def set_flags(self, copy: 'bool_t' = False, allows_duplicate_labels: 'bool_t | None' = None):
        return CallCol(lambda DF: self.__call__(DF).set_flags(copy, allows_duplicate_labels))

    def shift(self, periods: 'int' = 1, freq=None, axis: 'Axis' = 0, fill_value: 'Hashable' = None):
        return CallCol(lambda DF: self.__call__(DF).shift(periods, freq, axis, fill_value))

    def skew(self, axis: 'AxisInt | None' = 0, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).skew(axis, skipna, numeric_only, **kwargs))

    def sort_index(self, axis: 'Axis' = 0, level: 'IndexLabel' = None, ascending: 'bool | Sequence[bool]' = True, inplace: 'bool' = False, kind: 'SortKind' = 'quicksort', na_position: 'NaPosition' = 'last', sort_remaining: 'bool' = True, ignore_index: 'bool' = False, key: 'IndexKeyFunc' = None):
        return CallCol(lambda DF: self.__call__(DF).sort_index(axis, level, ascending, inplace, kind, na_position, sort_remaining, ignore_index, key))

    def sort_values(self, axis: 'Axis' = 0, ascending: 'bool | int | Sequence[bool] | Sequence[int]' = True, inplace: 'bool' = False, kind: 'str' = 'quicksort', na_position: 'str' = 'last', ignore_index: 'bool' = False, key: 'ValueKeyFunc' = None):
        return CallCol(lambda DF: self.__call__(DF).sort_values(axis, ascending, inplace, kind, na_position, ignore_index, key))

    def squeeze(self, axis: 'Axis | None' = None):
        return CallCol(lambda DF: self.__call__(DF).squeeze(axis))

    def std(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, ddof: 'int' = 1, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).std(axis, skipna, ddof, numeric_only, **kwargs))

    def sub(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).sub(decide_if_call(other, DF), level, fill_value, axis))

    def subtract(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).subtract(decide_if_call(other, DF), level, fill_value, axis))

    def sum(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, numeric_only: 'bool_t' = False, min_count: 'int' = 0, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).sum(axis, skipna, numeric_only, min_count, **kwargs))

    def swapaxes(self, axis1: 'Axis', axis2: 'Axis', copy: 'bool_t | None' = None):
        return CallCol(lambda DF: self.__call__(DF).swapaxes(axis1, axis2, copy))

    def swaplevel(self, i: 'Level' = -2, j: 'Level' = -1, copy: 'bool | None' = None):
        return CallCol(lambda DF: self.__call__(DF).swaplevel(i, j, copy))

    def tail(self, n: 'int' = 5):
        return CallCol(lambda DF: self.__call__(DF).tail(n))

    def take(self, indices, axis: 'Axis' = 0, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).take(indices, axis, **kwargs))

    def to_clipboard(self, excel: 'bool_t' = True, sep: 'str | None' = None, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).to_clipboard(excel, sep, **kwargs))

    def to_csv(self, path_or_buf: 'FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None' = None, sep: 'str' = ',', na_rep: 'str' = '', float_format: 'str | Callable | None' = None, columns: 'Sequence[Hashable] | None' = None, header: 'bool_t | list[str]' = True, index: 'bool_t' = True, index_label: 'IndexLabel | None' = None, mode: 'str' = 'w', encoding: 'str | None' = None, compression: 'CompressionOptions' = 'infer', quoting: 'int | None' = None, quotechar: 'str' = '"', lineterminator: 'str | None' = None, chunksize: 'int | None' = None, date_format: 'str | None' = None, doublequote: 'bool_t' = True, escapechar: 'str | None' = None, decimal: 'str' = '.', errors: 'str' = 'strict', storage_options: 'StorageOptions' = None):
        return CallCol(lambda DF: self.__call__(DF).to_csv(path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, decimal, errors, storage_options))

    def to_dict(self, into: 'type[dict]' = dict):
        return CallCol(lambda DF: self.__call__(DF).to_dict(into))

    def to_excel(self, excel_writer, sheet_name: 'str' = 'Sheet1', na_rep: 'str' = '', float_format: 'str | None' = None, columns: 'Sequence[Hashable] | None' = None, header: 'Sequence[Hashable] | bool_t' = True, index: 'bool_t' = True, index_label: 'IndexLabel' = None, startrow: 'int' = 0, startcol: 'int' = 0, engine: 'str | None' = None, merge_cells: 'bool_t' = True, inf_rep: 'str' = 'inf', freeze_panes: 'tuple[int, int] | None' = None, storage_options: 'StorageOptions' = None):
        return CallCol(lambda DF: self.__call__(DF).to_excel(excel_writer, sheet_name, na_rep, float_format, columns, header, index, index_label, startrow, startcol, engine, merge_cells, inf_rep, freeze_panes, storage_options))

    def to_frame(self, name: 'Hashable' = lib.no_default):
        return CallCol(lambda DF: self.__call__(DF).to_frame(name))

    def to_hdf(self, path_or_buf: 'FilePath | HDFStore', key: 'str', mode: 'str' = 'a', complevel: 'int | None' = None, complib: 'str | None' = None, append: 'bool_t' = False, format: 'str | None' = None, index: 'bool_t' = True, min_itemsize: 'int | dict[str, int] | None' = None, nan_rep=None, dropna: 'bool_t | None' = None, data_columns: 'Literal[True] | list[str] | None' = None, errors: 'str' = 'strict', encoding: 'str' = 'UTF-8'):
        return CallCol(lambda DF: self.__call__(DF).to_hdf(path_or_buf, key, mode, complevel, complib, append, format, index, min_itemsize, nan_rep, dropna, data_columns, errors, encoding))

    def to_json(self, path_or_buf: 'FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None' = None, orient: 'str | None' = None, date_format: 'str | None' = None, double_precision: 'int' = 10, force_ascii: 'bool_t' = True, date_unit: 'str' = 'ms', default_handler: 'Callable[[Any], JSONSerializable] | None' = None, lines: 'bool_t' = False, compression: 'CompressionOptions' = 'infer', index: 'bool_t' = True, indent: 'int | None' = None, storage_options: 'StorageOptions' = None, mode: "Literal['a', 'w']" = 'w'):
        return CallCol(lambda DF: self.__call__(DF).to_json(path_or_buf, orient, date_format, double_precision, force_ascii, date_unit, default_handler, lines, compression, index, indent, storage_options, mode))

    def to_latex(self, buf: 'FilePath | WriteBuffer[str] | None' = None, columns: 'Sequence[Hashable] | None' = None, header: 'bool_t | Sequence[str]' = True, index: 'bool_t' = True, na_rep: 'str' = 'NaN', formatters: 'FormattersType | None' = None, float_format: 'FloatFormatType | None' = None, sparsify: 'bool_t | None' = None, index_names: 'bool_t' = True, bold_rows: 'bool_t' = False, column_format: 'str | None' = None, longtable: 'bool_t | None' = None, escape: 'bool_t | None' = None, encoding: 'str | None' = None, decimal: 'str' = '.', multicolumn: 'bool_t | None' = None, multicolumn_format: 'str | None' = None, multirow: 'bool_t | None' = None, caption: 'str | tuple[str, str] | None' = None, label: 'str | None' = None, position: 'str | None' = None):
        return CallCol(lambda DF: self.__call__(DF).to_latex(buf, columns, header, index, na_rep, formatters, float_format, sparsify, index_names, bold_rows, column_format, longtable, escape, encoding, decimal, multicolumn, multicolumn_format, multirow, caption, label, position))

    def to_list(self):
        return CallCol(lambda DF: self.__call__(DF).to_list())

    def to_markdown(self, buf: 'IO[str] | None' = None, mode: 'str' = 'wt', index: 'bool' = True, storage_options: 'StorageOptions' = None, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).to_markdown(buf, mode, index, storage_options, **kwargs))

    def to_numpy(self, dtype: 'npt.DTypeLike | None' = None, copy: 'bool' = False, na_value: 'object' = lib.no_default, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).to_numpy(dtype, copy, na_value, **kwargs))

    def to_period(self, freq: 'str | None' = None, copy: 'bool | None' = None):
        return CallCol(lambda DF: self.__call__(DF).to_period(freq, copy))

    def to_pickle(self, path: 'FilePath | WriteBuffer[bytes]', compression: 'CompressionOptions' = 'infer', protocol: 'int' = 5, storage_options: 'StorageOptions' = None):
        return CallCol(lambda DF: self.__call__(DF).to_pickle(path, compression, protocol, storage_options))

    def to_sql(self, name: 'str', con, schema: 'str | None' = None, if_exists: "Literal['fail', 'replace', 'append']" = 'fail', index: 'bool_t' = True, index_label: 'IndexLabel' = None, chunksize: 'int | None' = None, dtype: 'DtypeArg | None' = None, method: 'str | None' = None):
        return CallCol(lambda DF: self.__call__(DF).to_sql(name, con, schema, if_exists, index, index_label, chunksize, dtype, method))

    def to_string(self, buf: 'FilePath | WriteBuffer[str] | None' = None, na_rep: 'str' = 'NaN', float_format: 'str | None' = None, header: 'bool' = True, index: 'bool' = True, length: 'bool' = False, dtype: 'bool' = False, name: 'bool' = False, max_rows: 'int | None' = None, min_rows: 'int | None' = None):
        return CallCol(lambda DF: self.__call__(DF).to_string(buf, na_rep, float_format, header, index, length, dtype, name, max_rows, min_rows))

    def to_timestamp(self, freq=None, how: "Literal['s', 'e', 'start', 'end']" = 'start', copy: 'bool | None' = None):
        return CallCol(lambda DF: self.__call__(DF).to_timestamp(freq, how, copy))

    def to_xarray(self):
        return CallCol(lambda DF: self.__call__(DF).to_xarray())

    def transform(self, func: 'AggFuncType', axis: 'Axis' = 0, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).transform(func, axis, *args, **kwargs))

    def transpose(self, *args, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).transpose(*args, **kwargs))

    def truediv(self, other, level=None, fill_value=None, axis: 'Axis' = 0):
        return CallCol(lambda DF: self.__call__(DF).truediv(decide_if_call(other, DF), level, fill_value, axis))

    def truncate(self, before=None, after=None, axis: 'Axis | None' = None, copy: 'bool_t | None' = None):
        return CallCol(lambda DF: self.__call__(DF).truncate(before, after, axis, copy))

    def tz_convert(self, tz, axis: 'Axis' = 0, level=None, copy: 'bool_t | None' = None):
        return CallCol(lambda DF: self.__call__(DF).tz_convert(tz, axis, level, copy))

    def tz_localize(self, tz, axis: 'Axis' = 0, level=None, copy: 'bool_t | None' = None, ambiguous: 'TimeAmbiguous' = 'raise', nonexistent: 'TimeNonexistent' = 'raise'):
        return CallCol(lambda DF: self.__call__(DF).tz_localize(tz, axis, level, copy, ambiguous, nonexistent))

    def unique(self):
        return CallCol(lambda DF: self.__call__(DF).unique())

    def unstack(self, level: 'IndexLabel' = -1, fill_value: 'Hashable' = None):
        return CallCol(lambda DF: self.__call__(DF).unstack(level, fill_value))

    def update(self, other: 'Series | Sequence | Mapping'):
        return CallCol(lambda DF: self.__call__(DF).update(decide_if_call(other, DF)))

    def value_counts(self, normalize: 'bool' = False, sort: 'bool' = True, ascending: 'bool' = False, bins=None, dropna: 'bool' = True):
        return CallCol(lambda DF: self.__call__(DF).value_counts(normalize, sort, ascending, bins, dropna))

    def var(self, axis: 'Axis | None' = None, skipna: 'bool_t' = True, ddof: 'int' = 1, numeric_only: 'bool_t' = False, **kwargs):
        return CallCol(lambda DF: self.__call__(DF).var(axis, skipna, ddof, numeric_only, **kwargs))

    def view(self, dtype: 'Dtype | None' = None):
        return CallCol(lambda DF: self.__call__(DF).view(dtype))

    def where(self, cond, other=lib.no_default):
        return CallCol(lambda DF: self.__call__(DF).where(decide_if_call(cond, DF), decide_if_call(other, DF)))

    def xs(self, key: 'IndexLabel', axis: 'Axis' = 0, level: 'IndexLabel' = None, drop_level: 'bool_t' = True):
        return CallCol(lambda DF: self.__call__(DF).xs(key, axis, level, drop_level))

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