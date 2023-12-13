# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._minpack, version:  1.10
import typing

__version__: str

def _chkder(m, n, x, fvec, fjac, ldfjac, xp, fvecp, mode, err) -> typing.Any: ...
def _hybrd(fun, x0, args, full_output, xtol, maxfev, ml, mu, epsfcn, factor, diag) -> typing.Any: ...
def _hybrj(fun, Dfun, x0, args, full_output, col_deriv, xtol, maxfev, factor, diag) -> typing.Any: ...
def _lmder(fun, Dfun, x0, args, full_output, col_deriv, ftol, xtol, gtol, maxfev, factor, diag) -> typing.Any: ...
def _lmdif(fun, x0, args, full_output, ftol, xtol, gtol, maxfev, epsfcn, factor, diag) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
