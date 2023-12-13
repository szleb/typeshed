# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.sparse.linalg.eigen.arpack._arpack, version: $Revision: $
import typing

__version__: bytes

def cnaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any: ...
def cneupd(
    rvec,
    howmny,
    select,
    sigma,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    rwork,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any: ...
def debug() -> typing.Any: ...
def dnaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any: ...
def dneupd(
    rvec,
    howmny,
    select,
    sigmar,
    sigmai,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any: ...
def dsaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any: ...
def dseupd(
    rvec,
    howmny,
    select,
    sigma,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any: ...
def snaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any: ...
def sneupd(
    rvec,
    howmny,
    select,
    sigmar,
    sigmai,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any: ...
def ssaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any: ...
def sseupd(
    rvec,
    howmny,
    select,
    sigma,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any: ...
def timing() -> typing.Any: ...
def znaupd(
    ido, bmat, which, nev, tol, resid, v, iparam, ipntr, workd, workl, rwork, info, n=..., ncv=..., ldv=..., lworkl=...
) -> typing.Any: ...
def zneupd(
    rvec,
    howmny,
    select,
    sigma,
    workev,
    bmat,
    which,
    nev,
    tol,
    resid,
    v,
    iparam,
    ipntr,
    workd,
    workl,
    rwork,
    info,
    ldz=...,
    n=...,
    ncv=...,
    ldv=...,
    lworkl=...,
) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
