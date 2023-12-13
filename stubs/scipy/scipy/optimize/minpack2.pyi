# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize.minpack2, version: $Revision: $
import typing

__version__: bytes

def dcsrch(stp, f, g, ftol, gtol, xtol, task, stpmin, stpmax, isave, dsave) -> typing.Any: ...
def dcstep(stx, fx, dx, sty, fy, dy, stp, fp, dp, brackt, stpmin, stpmax) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
