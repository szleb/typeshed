# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: _odrpack, version: unspecified
import typing

def _set_exceptions(odr_error, odr_stop) -> typing.Any: ...
def odr(
    fcn,
    beta0,
    y,
    x,
    we=...,
    wd=...,
    fjacb=...,
    fjacd=...,
    extra_args=...,
    ifixx=...,
    ifixb=...,
    job=...,
    iprint=...,
    errfile=...,
    rptfile=...,
    ndigit=...,
    taufac=...,
    sstol=...,
    partol=...,
    maxit=...,
    stpb=...,
    stpd=...,
    sclb=...,
    scld=...,
    work=...,
    iwork=...,
    full_output=...,
) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
