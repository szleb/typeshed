# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.linalg._interpolative, version: $Revision: $
import typing

__version__: bytes

def id_srand(n) -> typing.Any: ...
def id_srandi(t) -> typing.Any: ...
def id_srando() -> typing.Any: ...
def idd_copycols(a, krank, list, m=..., n=...) -> typing.Any: ...
def idd_diffsnorm(
    m,
    n,
    matvect,
    matvect2,
    matvec,
    matvec2,
    its,
    p1t=...,
    p2t=...,
    p3t=...,
    p4t=...,
    p1t2=...,
    p2t2=...,
    p3t2=...,
    p4t2=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    p12=...,
    p22=...,
    p32=...,
    p42=...,
    w=...,
    matvect_extra_args=...,
    matvect2_extra_args=...,
    matvec_extra_args=...,
    matvec2_extra_args=...,
) -> typing.Any: ...
def idd_estrank(eps, a, w, ra, m=..., n=...) -> typing.Any: ...
def idd_findrank(eps, m, n, matvect, p1=..., p2=..., p3=..., p4=..., w=..., matvect_extra_args=...) -> typing.Any: ...
def idd_frm(n, w, x, m=...) -> typing.Any: ...
def idd_frmi(m) -> typing.Any: ...
def idd_id2svd(b, list, proj, m=..., krank=..., n=..., w=...) -> typing.Any: ...
def idd_reconid(col, list, proj, m=..., krank=..., n=...) -> typing.Any: ...
def idd_reconint(list, proj, n=..., krank=...) -> typing.Any: ...
def idd_sfrm(l, n, w, x, m=...) -> typing.Any: ...
def idd_sfrmi(l, m) -> typing.Any: ...
def idd_snorm(
    m,
    n,
    matvect,
    matvec,
    its,
    p1t=...,
    p2t=...,
    p3t=...,
    p4t=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    u=...,
    matvect_extra_args=...,
    matvec_extra_args=...,
) -> typing.Any: ...
def iddp_aid(eps, a, work, proj, m=..., n=...) -> typing.Any: ...
def iddp_asvd(eps, a, winit, w, m=..., n=...) -> typing.Any: ...
def iddp_id(eps, a, m=..., n=...) -> typing.Any: ...
def iddp_rid(eps, m, n, matvect, proj, p1=..., p2=..., p3=..., p4=..., matvect_extra_args=...) -> typing.Any: ...
def iddp_rsvd(
    eps,
    m,
    n,
    matvect,
    matvec,
    p1t=...,
    p2t=...,
    p3t=...,
    p4t=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    matvect_extra_args=...,
    matvec_extra_args=...,
) -> typing.Any: ...
def iddp_svd(eps, a, m=..., n=...) -> typing.Any: ...
def iddr_aid(a, krank, w, m=..., n=...) -> typing.Any: ...
def iddr_aidi(m, n, krank) -> typing.Any: ...
def iddr_asvd(a, krank, w, m=..., n=...) -> typing.Any: ...
def iddr_id(a, krank, m=..., n=...) -> typing.Any: ...
def iddr_rid(m, n, matvect, krank, p1=..., p2=..., p3=..., p4=..., matvect_extra_args=...) -> typing.Any: ...
def iddr_rsvd(
    m,
    n,
    matvect,
    matvec,
    krank,
    p1t=...,
    p2t=...,
    p3t=...,
    p4t=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    w=...,
    matvect_extra_args=...,
    matvec_extra_args=...,
) -> typing.Any: ...
def iddr_svd(a, krank, m=..., n=..., r=...) -> typing.Any: ...
def idz_copycols(a, krank, list, m=..., n=...) -> typing.Any: ...
def idz_diffsnorm(
    m,
    n,
    matveca,
    matveca2,
    matvec,
    matvec2,
    its,
    p1a=...,
    p2a=...,
    p3a=...,
    p4a=...,
    p1a2=...,
    p2a2=...,
    p3a2=...,
    p4a2=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    p12=...,
    p22=...,
    p32=...,
    p42=...,
    w=...,
    matveca_extra_args=...,
    matveca2_extra_args=...,
    matvec_extra_args=...,
    matvec2_extra_args=...,
) -> typing.Any: ...
def idz_estrank(eps, a, w, ra, m=..., n=...) -> typing.Any: ...
def idz_findrank(eps, m, n, matveca, p1=..., p2=..., p3=..., p4=..., w=..., matveca_extra_args=...) -> typing.Any: ...
def idz_frm(n, w, x, m=...) -> typing.Any: ...
def idz_frmi(m) -> typing.Any: ...
def idz_id2svd(b, list, proj, m=..., krank=..., n=..., w=...) -> typing.Any: ...
def idz_reconid(col, list, proj, m=..., krank=..., n=...) -> typing.Any: ...
def idz_reconint(list, proj, n=..., krank=...) -> typing.Any: ...
def idz_sfrm(l, n, w, x, m=...) -> typing.Any: ...
def idz_sfrmi(l, m) -> typing.Any: ...
def idz_snorm(
    m,
    n,
    matveca,
    matvec,
    its,
    p1a=...,
    p2a=...,
    p3a=...,
    p4a=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    u=...,
    matveca_extra_args=...,
    matvec_extra_args=...,
) -> typing.Any: ...
def idzp_aid(eps, a, work, proj, m=..., n=...) -> typing.Any: ...
def idzp_asvd(eps, a, winit, w, m=..., n=...) -> typing.Any: ...
def idzp_id(eps, a, m=..., n=...) -> typing.Any: ...
def idzp_rid(eps, m, n, matveca, proj, p1=..., p2=..., p3=..., p4=..., matveca_extra_args=...) -> typing.Any: ...
def idzp_rsvd(
    eps,
    m,
    n,
    matveca,
    matvec,
    p1a=...,
    p2a=...,
    p3a=...,
    p4a=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    matveca_extra_args=...,
    matvec_extra_args=...,
) -> typing.Any: ...
def idzp_svd(eps, a, m=..., n=...) -> typing.Any: ...
def idzr_aid(a, krank, w, m=..., n=...) -> typing.Any: ...
def idzr_aidi(m, n, krank) -> typing.Any: ...
def idzr_asvd(a, krank, w, m=..., n=...) -> typing.Any: ...
def idzr_id(a, krank, m=..., n=...) -> typing.Any: ...
def idzr_rid(m, n, matveca, krank, p1=..., p2=..., p3=..., p4=..., matveca_extra_args=...) -> typing.Any: ...
def idzr_rsvd(
    m,
    n,
    matveca,
    matvec,
    krank,
    p1a=...,
    p2a=...,
    p3a=...,
    p4a=...,
    p1=...,
    p2=...,
    p3=...,
    p4=...,
    w=...,
    matveca_extra_args=...,
    matvec_extra_args=...,
) -> typing.Any: ...
def idzr_svd(a, krank, m=..., n=..., r=...) -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
