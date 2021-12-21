"""
Module for the :class:`pandas.Index` accessor class.

Currently, this module has no useful functionality.
"""

from pandas import Index
from pandas.api.extensions import register_index_accessor

from bpw_pde import ACCESSOR_NAME


@register_index_accessor(ACCESSOR_NAME)
class IndexAccessor:
    """Accessor class for :class:`pandas.Index`."""

    def __init__(self, index: Index) -> None:
        self._index = index
