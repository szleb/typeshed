# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.interpolate.interpnd, version: unspecified
import builtins as _mod_builtins
import typing

class NDInterpolatorBase(_mod_builtins.object):
    def __call__(self, *args) -> typing.Any: ...
    __dict__: dict[str, typing.Any]
    def __init__(self, points, values, fill_value, ndim, rescale, need_contiguous, need_values) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None: ...
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool: ...
    @property
    def __weakref__(self) -> typing.Any: ...
    def _check_call_shape(self, xi) -> typing.Any: ...
    def _scale_x(self, xi) -> typing.Any: ...
    def __getattr__(self, name) -> typing.Any: ...

class CloughTocher2DInterpolator(NDInterpolatorBase):
    __dict__: dict[str, typing.Any]
    def __init__(self, points, values, tol=...) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool: ...
    def _do_evaluate(self, xi, dummy) -> typing.Any: ...
    def _evaluate_complex(self, xi) -> typing.Any: ...
    def _evaluate_double(self, xi) -> typing.Any: ...
    def __getattr__(self, name) -> typing.Any: ...

class GradientEstimationWarning(_mod_builtins.Warning):
    __dict__: dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None: ...
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool: ...
    @property
    def __weakref__(self) -> typing.Any: ...
    def __getattr__(self, name) -> typing.Any: ...

class LinearNDInterpolator(NDInterpolatorBase):
    __dict__: dict[str, typing.Any]
    def __init__(self, points, values, fill_value=..., rescale=...) -> None: ...
    @classmethod
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool: ...
    def _do_evaluate(self, xi, dummy) -> typing.Any: ...
    def _evaluate_complex(self, xi) -> typing.Any: ...
    def _evaluate_double(self, xi) -> typing.Any: ...
    def __getattr__(self, name) -> typing.Any: ...

def __pyx_unpickle_Enum() -> typing.Any: ...

__test__: dict

def _ndim_coords_from_arrays() -> typing.Any: ...
def estimate_gradients_2d_global() -> typing.Any: ...
def __getattr__(name) -> typing.Any: ...
