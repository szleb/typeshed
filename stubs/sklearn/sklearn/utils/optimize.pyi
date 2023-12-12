# This is a modified file from scipy.optimize
# Original authors: Travis Oliphant, Eric Jones
# Modifications by Gael Varoquaux, Mathieu Blondel and Tom Dupre la Tour
# License: BSD

from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .fixes import line_search_wolfe1 as line_search_wolfe1, line_search_wolfe2 as line_search_wolfe2

class _LineSearchError(RuntimeError): ...
