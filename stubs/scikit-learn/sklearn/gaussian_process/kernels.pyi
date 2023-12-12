from abc import ABCMeta, abstractmethod
from collections import namedtuple
from inspect import signature as signature
from typing import Callable, Literal, Sequence, TypeVar

from numpy import ndarray
from scipy.spatial.distance import cdist as cdist, pdist as pdist, squareform as squareform
from scipy.special import kv as kv

from .._typing import ArrayLike, Float, MatrixLike
from ..base import clone as clone
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics.pairwise import pairwise_kernels as pairwise_kernels

Kernel_Self = TypeVar("Kernel_Self", bound=Kernel)
Hyperparameter_Self = TypeVar("Hyperparameter_Self", bound=Hyperparameter)

class Hyperparameter(namedtuple("Hyperparameter", ("name", "value_type", "bounds", "n_elements", "fixed"))):
    fixed: bool = ...
    n_elements: int = ...
    bounds: tuple[float, float] | str = ...
    value_type: str = ...
    name: str = ...

    # A raw namedtuple is very memory efficient as it packs the attributes
    # in a struct to get rid of the __dict__ of attributes in particular it
    # does not copy the string for the keys on each instance.
    # By deriving a namedtuple class just to introduce the __init__ method we
    # would also reintroduce the __dict__ on the instance. By telling the
    # Python interpreter that this subclass uses static __slots__ instead of
    # dynamic attributes. Furthermore we don't need any additional slot in the
    # subclass so we set __slots__ to the empty tuple.
    __slots__ = ...

    def __new__(
        cls,
        name: str,
        value_type: str,
        bounds: ndarray | str | tuple[float, int] | tuple[float, float],
        n_elements: int = 1,
        fixed=None,
    ) -> Hyperparameter: ...

    # This is mainly a testing utility to check that two hyperparameters
    # are equal.
    def __eq__(self, other) -> bool: ...

class Kernel(metaclass=ABCMeta):
    def get_params(self, deep: bool = True) -> dict: ...
    def set_params(self: Kernel_Self, **params) -> Kernel_Self: ...
    def clone_with_theta(self, theta: ArrayLike) -> None: ...
    def n_dims(self) -> int: ...
    def hyperparameters(self) -> list[Hyperparameter]: ...
    @property
    def theta(self) -> ndarray: ...
    @theta.setter
    def theta(self, theta) -> ndarray: ...
    @property
    def bounds(self) -> ndarray: ...
    def __add__(self, b) -> Sum: ...
    def __radd__(self, b): ...
    def __mul__(self, b) -> Product: ...
    def __rmul__(self, b: float | int) -> Product: ...
    def __pow__(self, b: int) -> Exponentiation: ...
    def __eq__(self, b: str) -> bool: ...
    @abstractmethod
    def __call__(self, X, Y=None, eval_gradient: bool = False): ...
    @abstractmethod
    def diag(self, X: ArrayLike) -> ndarray: ...
    @abstractmethod
    def is_stationary(self) -> None: ...
    def requires_vector_input(self) -> bool: ...

class NormalizedKernelMixin:
    def diag(self, X: MatrixLike) -> ndarray: ...

class StationaryKernelMixin:
    def is_stationary(self) -> None: ...

class GenericKernelMixin:
    def requires_vector_input(self) -> bool: ...

class CompoundKernel(Kernel):
    def __init__(self, kernels: Sequence[Kernel]) -> None: ...
    def get_params(self, deep: bool = True) -> dict: ...
    @property
    def theta(self) -> ndarray: ...
    @theta.setter
    def theta(self, theta) -> ndarray: ...
    @property
    def bounds(self) -> ndarray: ...
    def __call__(
        self, X: MatrixLike | ArrayLike, Y: None | MatrixLike | ArrayLike = None, eval_gradient: bool = False
    ) -> tuple[ndarray, ndarray]: ...
    def __eq__(self, b) -> bool: ...
    def is_stationary(self) -> None: ...
    def requires_vector_input(self) -> None: ...
    def diag(self, X: MatrixLike | ArrayLike) -> ndarray: ...

class KernelOperator(Kernel):
    def __init__(self, k1, k2) -> None: ...
    def get_params(self, deep: bool = True) -> dict: ...
    def hyperparameters(self) -> list[Hyperparameter]: ...
    @property
    def theta(self) -> ndarray: ...
    @theta.setter
    def theta(self, theta) -> ndarray: ...
    @property
    def bounds(self) -> ndarray: ...
    def __eq__(self, b) -> bool: ...
    def is_stationary(self) -> None: ...
    def requires_vector_input(self) -> bool: ...

class Sum(KernelOperator):
    def __call__(
        self, X: MatrixLike | ArrayLike, Y: None | MatrixLike | ArrayLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def diag(self, X: MatrixLike | ArrayLike) -> ndarray: ...

class Product(KernelOperator):
    def __call__(
        self, X: MatrixLike | ArrayLike, Y: Sequence | None | MatrixLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def diag(self, X: MatrixLike | ArrayLike) -> ndarray: ...

class Exponentiation(Kernel):
    def __init__(self, kernel: DotProduct | Kernel, exponent: Float) -> None: ...
    def get_params(self, deep: bool = True) -> dict[str, DotProduct | int] | dict: ...
    def hyperparameters(self) -> list[Hyperparameter]: ...
    @property
    def theta(self) -> ndarray: ...
    @theta.setter
    def theta(self, theta) -> ndarray: ...
    @property
    def bounds(self) -> ndarray: ...
    def __eq__(self, b) -> bool: ...
    def __call__(
        self, X: MatrixLike | ArrayLike, Y: Sequence | None | MatrixLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def diag(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def is_stationary(self) -> None: ...
    def requires_vector_input(self) -> bool: ...

class ConstantKernel(StationaryKernelMixin, GenericKernelMixin, Kernel):
    def __init__(self, constant_value: Float = 1.0, constant_value_bounds: str | tuple[float, float] = ...) -> None: ...
    def hyperparameter_constant_value(self) -> Hyperparameter: ...
    def __call__(
        self, X: MatrixLike | ArrayLike, Y: None | MatrixLike | ArrayLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def diag(self, X: MatrixLike | ArrayLike) -> ndarray: ...

class WhiteKernel(StationaryKernelMixin, GenericKernelMixin, Kernel):
    def __init__(self, noise_level: Float = 1.0, noise_level_bounds: str | tuple[float, float] = ...) -> None: ...
    def hyperparameter_noise_level(self) -> Hyperparameter: ...
    def __call__(
        self, X: MatrixLike | ArrayLike, Y: None | MatrixLike | ArrayLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def diag(self, X: MatrixLike | ArrayLike) -> ndarray: ...

class RBF(StationaryKernelMixin, NormalizedKernelMixin, Kernel):
    def __init__(self, length_scale: ArrayLike | Float = 1.0, length_scale_bounds: str | tuple[float, float] = ...) -> None: ...
    def anisotropic(self) -> bool: ...
    def hyperparameter_length_scale(self) -> Hyperparameter: ...
    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...

class Matern(RBF):
    def __init__(
        self, length_scale: ArrayLike | Float = 1.0, length_scale_bounds: str | tuple[float, float] = ..., nu: Float = 1.5
    ) -> None: ...
    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...

class RationalQuadratic(StationaryKernelMixin, NormalizedKernelMixin, Kernel):
    def __init__(
        self,
        length_scale: Float = 1.0,
        alpha: Float = 1.0,
        length_scale_bounds: str | tuple[float, float] = ...,
        alpha_bounds: str | tuple[float, float] = ...,
    ) -> None: ...
    def hyperparameter_length_scale(self) -> Hyperparameter: ...
    def hyperparameter_alpha(self) -> Hyperparameter: ...
    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...

class ExpSineSquared(StationaryKernelMixin, NormalizedKernelMixin, Kernel):
    def __init__(
        self,
        length_scale: Float = 1.0,
        periodicity: Float = 1.0,
        length_scale_bounds: str | tuple[float, float] = ...,
        periodicity_bounds: str | tuple[float, float] = ...,
    ) -> None: ...
    def hyperparameter_length_scale(self) -> Hyperparameter: ...
    def hyperparameter_periodicity(self) -> Hyperparameter: ...
    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...

class DotProduct(Kernel):
    def __init__(self, sigma_0: Float = 1.0, sigma_0_bounds: str | tuple[float, float] = ...) -> None: ...
    def hyperparameter_sigma_0(self) -> Hyperparameter: ...
    def __call__(
        self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False
    ) -> ndarray | tuple[ndarray, ndarray]: ...
    def diag(self, X: MatrixLike) -> ndarray: ...
    def is_stationary(self) -> None: ...

class PairwiseKernel(Kernel):
    def __init__(
        self,
        gamma: Float = 1.0,
        gamma_bounds: str | tuple[float, float] = ...,
        metric: Literal[
            "linear", "additive_chi2", "chi2", "poly", "polynomial", "rbf", "laplacian", "sigmoid", "cosine", "linear"
        ]
        | Callable = "linear",
        pairwise_kernels_kwargs: None | dict = None,
    ) -> None: ...
    def hyperparameter_gamma(self) -> None: ...
    def __call__(self, X: MatrixLike, Y: None | MatrixLike = None, eval_gradient: bool = False) -> tuple[ndarray, ndarray]: ...
    def diag(self, X: MatrixLike) -> ndarray: ...
    def is_stationary(self) -> None: ...
