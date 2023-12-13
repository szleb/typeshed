# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.optimize._trlib._trlib, version: unspecified
import typing

import scipy.optimize._trustregion as _mod_scipy_optimize__trustregion

BaseQuadraticSubproblem = _mod_scipy_optimize__trustregion.BaseQuadraticSubproblem

class TRLIBQuadraticSubproblem(_mod_scipy_optimize__trustregion.BaseQuadraticSubproblem):
    __dict__: dict[str, typing.Any]
    def __init__(self, x, fun, jac, hess, hessp, tol_rel_i, tol_rel_b, disp) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None: ...
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool: ...
    def solve(self, trust_radius) -> typing.Any: ...
    def __getattr__(self, name) -> typing.Any: ...

def __pyx_unpickle_Enum() -> typing.Any: ...

__test__: dict

def _minimize_trust_region(
    fun,
    x0,
    args,
    jac,
    hess,
    hessp,
    subproblem,
    initial_trust_radius,
    max_trust_radius,
    eta,
    gtol,
    maxiter,
    disp,
    return_all,
    callback,
    inexact,
    **unknown_options,
) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
