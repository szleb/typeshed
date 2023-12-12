from typing import Any, ClassVar, TypeVar
from scipy import linalg as linalg, sparse as sparse
from ._base import _BasePCA
from numpy import ndarray
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import svd_flip as svd_flip
from numbers import Integral as Integral
from .._typing import Int, MatrixLike, ArrayLike
from ..utils import gen_batches as gen_batches

IncrementalPCA_Self = TypeVar("IncrementalPCA_Self", bound="IncrementalPCA")

import numpy as np

class IncrementalPCA(_BasePCA):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    batch_size_: int = ...
    n_samples_seen_: int = ...
    n_components_: int = ...
    noise_variance_: float = ...
    var_: ndarray = ...
    mean_: ndarray = ...
    singular_values_: ndarray = ...
    explained_variance_ratio_: ndarray = ...
    explained_variance_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, n_components: None | Int = None, *, whiten: bool = False, copy: bool = True, batch_size: None | Int = None
    ) -> None: ...
    def fit(self: IncrementalPCA_Self, X: MatrixLike | ArrayLike, y: Any = None) -> IncrementalPCA_Self: ...
    def partial_fit(self: IncrementalPCA_Self, X: MatrixLike, y: Any = None, check_input: bool = True) -> IncrementalPCA_Self: ...
    def transform(self, X: MatrixLike | ArrayLike) -> ndarray: ...
