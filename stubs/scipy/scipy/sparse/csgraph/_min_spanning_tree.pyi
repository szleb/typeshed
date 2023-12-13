# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.sparse.csgraph._min_spanning_tree, version: unspecified
import typing

import numpy as _mod_numpy

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32

def __pyx_unpickle_Enum() -> typing.Any: ...

__test__: dict

def isspmatrix(x) -> typing.Any: ...
def isspmatrix_csc(x) -> typing.Any: ...
def minimum_spanning_tree(csgraph, overwrite=...) -> typing.Any: ...
def validate_graph(
    csgraph,
    directed,
    dtype,
    csr_output,
    dense_output,
    copy_if_dense,
    copy_if_sparse,
    null_value_in,
    null_value_out,
    infinity_null,
    nan_null,
) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
