# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.interpolate.dfitpack, version: $Revision: $
import typing

__version__: bytes

def bispeu(tx, ty, c, kx, ky, x, y) -> typing.Any: ...
def bispev(tx, ty, c, kx, ky, x, y) -> typing.Any: ...
def curfit(iopt, x, y, w, t, wrk, iwrk, xb=..., xe=..., k=..., s=...) -> typing.Any: ...
def dblint(tx, ty, c, kx, ky, xb, xe, yb, ye) -> typing.Any: ...
def fpchec(x, t, k) -> typing.Any: ...
def fpcurf0(x, y, k, w=..., xb=..., xe=..., s=..., nest=...) -> typing.Any: ...
def fpcurf1(
    x,
    y,
    w,
    xb,
    xe,
    k,
    s,
    n,
    t,
    c,
    fp,
    fpint,
    nrdata,
    ier,
    overwrite_x=...,
    overwrite_y=...,
    overwrite_w=...,
    overwrite_t=...,
    overwrite_c=...,
    overwrite_fpint=...,
    overwrite_nrdata=...,
) -> typing.Any: ...
def fpcurfm1(x, y, k, t, w=..., xb=..., xe=..., overwrite_t=...) -> typing.Any: ...
def parcur(iopt, ipar, idim, u, x, w, ub, ue, t, wrk, iwrk, k=..., s=...) -> typing.Any: ...
def parder(tx, ty, c, kx, ky, nux, nuy, x, y) -> typing.Any: ...
def pardeu(tx, ty, c, kx, ky, nux, nuy, x, y) -> typing.Any: ...
def percur(iopt, x, y, w, t, wrk, iwrk, k=..., s=...) -> typing.Any: ...
def regrid_smth(x, y, z, xb=..., xe=..., yb=..., ye=..., kx=..., ky=..., s=...) -> typing.Any: ...
def regrid_smth_spher(iopt, ider, u, v, r, r0=..., r1=..., s=...) -> typing.Any: ...
def spalde(t, c, k, x) -> typing.Any: ...
def spherfit_lsq(teta, phi, r, tt, tp, w=..., eps=..., overwrite_tt=..., overwrite_tp=...) -> typing.Any: ...
def spherfit_smth(teta, phi, r, w=..., s=..., eps=...) -> typing.Any: ...
def splder(t, c, k, x, nu=..., e=...) -> typing.Any: ...
def splev(t, c, k, x, e=...) -> typing.Any: ...
def splint(t, c, k, a, b) -> typing.Any: ...
def sproot(t, c, mest=...) -> typing.Any: ...
def surfit_lsq(
    x,
    y,
    z,
    nx,
    tx,
    ny,
    ty,
    w=...,
    xb=...,
    xe=...,
    yb=...,
    ye=...,
    kx=...,
    ky=...,
    eps=...,
    lwrk2=...,
    overwrite_tx=...,
    overwrite_ty=...,
) -> typing.Any: ...
def surfit_smth(
    x, y, z, w=..., xb=..., xe=..., yb=..., ye=..., kx=..., ky=..., s=..., nxest=..., nyest=..., eps=..., lwrk2=...
) -> typing.Any: ...
def types() -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
