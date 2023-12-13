# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.signal.sigtools, version: unspecified
import typing

def _convolve2d(in1, in2, flip, mode, boundary, fillvalue) -> typing.Any: ...
def _correlateND(a, kernel, mode) -> typing.Any: ...
def _linear_filter() -> typing.Any: ...
def _medfilt2d() -> typing.Any: ...
def _order_filterND(a, domain, order) -> typing.Any: ...
def _remez(numtaps, bands, des, weight, type, fs, maxiter, grid_density) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
